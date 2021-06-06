require 'sorcerer'
require 'pp'

module RailsBestPractices
  module Reviews
    class PrintQueryReview < Review
      interesting_nodes :def, :defs, :command, :call, :module, :class, :method_add_arg, :method_add_block, :do_block, :brace_block, :assign
      interesting_files SPEC_FILES, CONTROLLER_FILES, MODEL_FILES, LIB_FILES, HELPER_FILES, VIEW_FILES, EXTRA_FILES
      url 'https://rails-bestpractices.com/posts/2010/10/03/use-query-attribute/'

      MULTI_QUERY_METHODS = %w[where where! pluck distinct eager_load from group having includes joins left_outer_joins limit offset order reload preload readonly reorder select reselect select_all reverse_order unscope find_each rewhere execute uniq all references].freeze
      SINGLE_QUERY_METHODS = %w[find find! take take! first first! last last! find_by find_by! create create! count].freeze

      def initialize(options = {})
        super(options)
        @collected_queries = []
        @scopes = {}
				@local_variable ||= {}
				@model_attrs ||= {}
        @output_filename_query = options['output_filename_query']
        @output_filename_scope = options['output_filename_scope']
				@output_filename_schema = options['output_filename_schema']
        @combined_class_name = ""
      end

      add_callback :end_module, :end_class do |node|
        @combined_class_name = ""
      end

      add_callback :start_module do |node|
        # puts "FILE #{node.file} #{node.sexp_type} #{node} #{to_source(node).chomp}"
        @current_class_name = node.module_name.to_s
        @combined_class_name += node.module_name.to_s
      end

      add_callback :start_class do |node|
        @current_class_name = node.class_name.to_s
        @combined_class_name += node.class_name.to_s
				@local_variable ||= {}
      end
      
      add_callback :after_check do
				collect_schema
	
        File.open(@output_filename_query, 'wb') {|f| f.write(Marshal.dump(@collected_queries))}
        puts "Query output written to #{@output_filename_query}"
        File.open(@output_filename_scope, 'wb') {|f| f.write(Marshal.dump(@scopes))}
        puts "Scope output written to #{@output_filename_scope}"
        File.open(@output_filename_schema, 'wb') {|f| f.write(Marshal.dump(@model_attrs))}
        puts "Scope output written to #{@output_filename_schema}"
      end


      add_callback :start_def, :start_defs, :start_call, :start_command, :start_do_block, :start_brace_block do |node|
        # puts "FILE #{node.file} #{node.sexp_type} #{node} #{to_source(node).chomp}"
        if node.sexp_type == :def or node.sexp_type == :defs
              node.recursive_children do |child|
                begin
                  if is_method_call?(child)
                    r = process_method_call_node(child, "")
                  elsif child.sexp_type == :assign && child[2] && is_method_call?(child[2])
                    r = process_method_call_node(child[2], "")
										if r != nil
										  @local_variable.store(child[1].to_s, to_source(child))
										end
                  end
                rescue => error
                end
              end
          elsif is_method_call?(node)
            process_method_call_node(node, "")
          elsif node.sexp_type == :do_block or node.sexp_type  == :brace_block
            bnode = node.children[-1]
            if bnode.sexp_type == :bodystmt
              # puts "type #{node.children[-1].children[-1].recursive_children}"
              # process_method_call_node(node.children[-1].children[-1], "")
              #puts "HERE #{node.children}"
              node.recursive_children do |child|
                begin
                  # puts "child #{to_source(child).chomp} #{child.sexp_type}"
                  if child.sexp_type == :stmts_add
                    # puts "child #{child[2].children}"
                    process_method_call_node(child[2], "")
                  elsif child.sexp_type == :field
                    process_method_call_node(child, "")
                  end
                rescue
                end
              end
           
           end
		  		elsif node.sexp_type == :command
            case node.message.to_s
          	  when 'named_scope', 'scope', 'has_many'
          			process_scope(node)
          			scope_name = node.arguments.all[0].to_s
								node.arguments.all[1].recursive_children do |child|
            			begin
              			if child.sexp_type == :stmts_add
											process_method_call_node(child[2], scope_name)
										end
									rescue => error
									end
								end
          	  end
          end
      end

			def collect_schema 
				model_hash = models.map{|model| [model.class_name, model]}.to_h
				nochange = false
				model_attribs = models.map{|model| [model.class_name, model_attributes.get_attribute_for(model.class_name)]}.to_h
				model_assocs = models.map{|model| [model.class_name, model_associations.get_association_for(model.class_name)]}.to_h
				while !nochange
					nochange = true
					models.each do |model|
						if !model_hash[model.extend_class_name].nil?
							if model_attribs[model.extend_class_name]["type"].nil?
								model_attribs[model.extend_class_name]["type"] = "string"
							end
							model_attribs[model.extend_class_name].each do |field,type|
								if model_attribs[model.class_name][field].nil?
									nochanged = false
									model_attribs[model.class_name][field] = type
								end
							end
							model_assocs[model.extend_class_name].each do |name,assoc|
								if model_assocs[model.class_name][name].nil?
									nochange = false
									model_assocs[model.class_name][name] = assoc
								end
							end
						end
					end
				end
				models.each do |model|
					x = model_attribs[model.class_name]
					y = model_assocs[model.class_name]
					@model_attrs[model] = {:fields => x, :associations => y.map{ |name,assoc| {:class_name=>assoc['class_name'].to_s, :rel=>assoc['meta'], :field=>name} }, :extend_class_name => model.extend_class_name }
					#puts "Model #{model.class_name}, extends #{model.extend_class_name}"
					#puts "\tfields = #{x.inspect}"
					#puts "\tassocs = #{y.map{|n,a| n+'->'+a['class_name']}.join(', ')}"
				end
			end

      def is_method_call?(node)
        return [:method_add_arg, :call].include?node.sexp_type
      end
			def is_call_node?(node)
				return node.sexp_type == :call
			end
      
      def process_method_call_node(node, func_name)
				is_scope = ->() {func_name!=""}
        @processed_node ||= []
        # puts "include: #{node} #{@processed_node.include?(node)}"
        # return nil if @processed_node.include?(node)
        cnt = 0

        @processed_node << node

        # puts "processed_node length #{ @processed_node.length}"
        call_node = nil
        node_list = []
        #if is_call_node?(node) 
        # puts "is method_call #{is_method_call?node}"
				if is_method_call?(node)
					call_node = node
				elsif (is_scope.call() and node.sexp_type == :command)
					call_node = node
        elsif node.sexp_type == :field
          call_node = node
				else
          node.children.each do |child| 
            if is_call_node?(child) #is_method_call?(child) 
              call_node = child
            end
          end
        end
        if call_node == nil
          node.recursive_children do |child|
            if is_method_call?child
              # puts "\t\tchild #{child} #{is_method_call?child}"
              process_method_call_node(child, "")
            end
          end
        end
				return nil if call_node == nil

				node_list << call_node
        call_node.recursive_children do |child|
          if [:call, :var_ref].include?(child.sexp_type) 
            node_list << child
          end
        end
        # initialize caller_class_lst
        caller_class_lst ||= []
				if is_scope.call()
					caller_class_lst << {:method=>call_node.message.to_s, :class=>@current_class_name}
				else
        	variable_node = variable(call_node)
          # puts "@@@ variable_node #{variable_node} is_mode: #{is_model?(variable_node)} is_query: #{is_query_function?(node)}"
          return nil if !is_model?(variable_node) && !is_query_function?(node)
					variable_node = variable_node.blank? ? node : variable_node
          class_name = get_class_name(variable_node)
          meth = {:method=>variable_node.to_s, :class=>class_name}	
          caller_class_lst << meth
				end
        
			
				if !is_scope.call()	
          @processed_node = @processed_node + node_list
        	contain_query = false
        	classes ||= [class_name]
          node_list.reverse.each do |cnode|
        	  fcall_name = cnode.message.to_s
            if model_association?(class_name, fcall_name)
        	    class_name = model_association?(class_name, fcall_name)['class_name']
        	    classes << class_name
        	  elsif model_method?(class_name, fcall_name)
        	    meth = model_method?(class_name, fcall_name)
        	  end
						if !fcall_name.nil?
							caller_class_lst << {:method => fcall_name, :class => class_name}
						end
        	end
				end
        # add processed nodes
				node.recursive_children do |child|
          if [:method_add_arg, :method_add_block, :call].include?child.sexp_type
            @processed_node << child
            cnt +=1
          end
        end
        source = to_source(node).chomp
        puts "source is #{source}"
        #if (MULTI_QUERY_METHODS+SINGLE_QUERY_METHODS).map{|x| source.include?(x)}.any?
        q = {:class => @combined_class_name, :stmt => source, :caller_class_lst => caller_class_lst, :method_name => func_name, :filename => @node.file, :line => node.line_number.to_i}
        @collected_queries << q
        # queries_sameline = @collected_queries.detect{|x| x[:filename] == q[:filename] and x[:line] == q[:line] and x[:stmt].include?q[:stmt]}
        # unique = true
        # queries_sameline.each do |q_same|
        #   if q_same.stmt.include?q.stmt
        #     unique = false
        #     break
        #   end
        # end
        # puts "UNIQUE #{unique}"
        # @collected_queries << q if unique
        #end
      end

      def process_scope(node)
        begin
          scope_name = node.arguments.all[0].to_s

          scope_def = nil
          node.arguments.all[1].recursive_children do |child|
            begin
              if child.sexp_type == :stmts_add
                scope_def = child
                break
              end
            rescue
            end
          end

          scope_def = to_source(scope_def).strip

          if (MULTI_QUERY_METHODS+SINGLE_QUERY_METHODS).map{|x| scope_def.include?(x)}.any?
            key = @current_class_name + "-" + scope_name
            @scopes[key] = scope_def
          end
        rescue
        end
      end

			def is_self?(variable_node)
        if variable_node.sexp_type == :var_ref && variable_node.to_s == "self"
          return models.include?(@current_class_name)
        end
        return false
      end
	
      def is_model?(variable_node)
        if is_self?(variable_node)
          return true
				elsif is_query_function?(variable_node)
					return !@current_class_name.nil?
        elsif variable_node.const?
          class_name = variable_node.to_s
        else
          # puts "#{variable_node.to_s.sub(/^@/, '').gsub(/[0-9]/, '')}"
          # puts "variable_node #{variable_node}"
          variable_node = "user" if variable_node.to_s == "current_user"
          variable_node = "post" if variable_node.to_s == "fetched_post"
          variable_node = "post" if variable_node.to_s == "new_post"
          variable_node = "person" if ["head", "child", "spouse", "new_child", "p"].include?variable_node.to_s
          variable_node = "family" if ["subject"].include?variable_node.to_s
          class_name = variable_node.to_s.sub(/^@/, '').sub(/[0-9]/, '').classify
        end
        models.include?(class_name)
      end
			
			def is_query_function?(node)
        return (MULTI_QUERY_METHODS+SINGLE_QUERY_METHODS).include?(node.message.to_s)
			end

      def get_class_name(variable_node)
        if is_self?(variable_node) || is_query_function?(variable_node) 
         	return @current_class_name 
        elsif variable_node.const?
          return variable_node.to_s
        else
          return variable_node.to_s.sub(/^@/, '').sub(/[0-9]/,'').classify
        end
      end

			def model_association?(class_name, message)
        assoc_type = model_associations.get_association(class_name, message)
        assoc_type
      end
      def model_method?(class_name, message)
        method = model_methods.get_method(class_name, message)
        method
      end

      def to_source(node)
        return Sorcerer.source(node, multiline:false, indent:2)
      end
    end
  end
end
