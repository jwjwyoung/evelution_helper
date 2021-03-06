require 'rails_best_practices'
require 'yard'
require 'open3'
require 'active_support'
require 'pg_query'
require "active_support/core_ext/string"
require_relative '../formatchecker/constraint_analyzer/helper.rb'
require File.join(File.expand_path(File.dirname(__FILE__)), './types.rb')
require File.join(File.expand_path(File.dirname(__FILE__)), './util.rb')
require File.join(File.expand_path(File.dirname(__FILE__)), './pg_extension.rb')
require File.join(File.expand_path(File.dirname(__FILE__)), './query_parser.rb')

# global variable; avoid passing as parameter...
$schema = nil
$scopes = nil
$query_map = {}


def is_valid_table?(table)
	$schema.each do |t|
		#puts "t #{t}"
		tclass = canonicalize_classname(t[:class_name].class_name)
		if table.to_s == tclass or tablename_singularize(table.to_s) == tclass
			return true
		end
	end
	return false
end

def find_table_in_schema(table)
	$schema.each do |t|
		tclass = canonicalize_classname(t[:class_name].class_name)
		if table.to_s == tclass or tablename_singularize(table.to_s) == tclass
			return t
		end
	end	
	#puts "Table #{table} (#{tablename_singularize(table)}) cannot be found in schema!"
	#puts "schema: "
	#$schema.each do |t|
	#	puts "\t #{t[:class_name]} --> #{table.to_s == t[:class_name].to_s} #{t.inspect}"
	#end
	#exit
	return nil
end

def find_scope(table, meth)
	return $scopes[table].nil? ? nil : $scopes[table][meth]
end

def get_fields_and_tables_for_query(components)
	fields = []
	components.each do |component|
		if component.is_a?(QueryColumn)
				fields << component
		elsif component.is_a?(QueryPredicate)
			if component.lh.is_a?(QueryColumn)
				fields << component.lh
			end
			if component.rh.is_a?(QueryColumn)
				fields << component.rh
			end
		elsif component.is_a?(Hash) # placeholder for scope
			fields << component
		end
	end
	#fields.uniq { |f| [canonicalize_classname(tablename_pluralize(f.table)), f.column] }	
	fields
end

def resolve_scopes(query)
	more_fields = []
	remove_fields = []
	source = ""
	query.fields.each do |f|
		if f.is_a?(Hash)
			scope_query = find_scope(f[:class], f[:meth])
			more_fields += $query_map[scope_query].fields
			remove_fields << f
			source += "\n\tscope #{f[:class]}:#{scope_query[:method_name]}: #{scope_query.stmt}"
		end
	end
	query.fields = (query.fields - remove_fields + more_fields).select{|x|!x.is_a?(Hash)}.uniq { |f| [tablename_pluralize(f.table), f.column] }	
	query.source += source
	# if more_fields.length > 0
	# 	puts "new source = #{query.source}"
	# 	puts "fields = #{query.fields}"
	# 	puts '"'
	# end
	query
end

def extract_query(ast)
  node = ast.type == :list ? ast[0] : ast
  if node.type == :assign and node[1].type == :call
    return node[1] 
  elsif node.type == :call or node.type == :fcall
		return node 
	elsif node.type == :command 
		return node
  end
end

def get_all_methods(node)
  return [] if node == nil

  if node.type == :call
    return get_all_methods(node[0]) + get_all_methods(node[2])
  elsif node.type == :fcall || node.type == :vcall
    return [node[0][0]]
  elsif node.type == :ident
    return [node[0]]
  else
    return []
  end
end

def find_first_string_in_node(node)
	if !is_valid_node?(node)
		return ""
	end
	if node.type == :string_content
		return node.source
	end
	node.each do |child|
		x = find_first_string_in_node(child)
		if !x.nil?
			return x
		end
	end
	""
end

def find_string_from_param(source)
	begin
		open('__temp_ruby_code_buffer.rbout', 'w') { |f|
  		f.puts "puts #{source}"
		}
		stdout, stderr, status = Open3.capture3("ruby __temp_ruby_code_buffer.rbout")
		return stdout
	rescue
		""
	end
end

def find_first_symbol_in_node(node)
	if !is_valid_node?(node)
		return ""
	end
	if node.type == :symbol_literal
		return node[0][0].source
	end
	node.each do |child|
		x = find_first_symbol_in_node(child)
		if !x.nil?
			return x
		end
	end
	""
end

def parse_partial_predicate(query, table, call_ident)
	base_table = tablename_pluralize(table)
	sql = "SELECT #{base_table}.id FROM #{base_table} WHERE #{query}"
	if query.upcase.start_with?("SELECT")
		sql = query
	elsif query.upcase.start_with?("INNER JOIN") or query.upcase.start_with?("LEFT") or query.upcase.start_with?("JOIN")
		sql = "SELECT #{base_table}.id FROM #{base_table} #{query}"
	elsif ["order", "reorder"].include?call_ident[0].to_s and !query.upcase.start_with?("ORDER")
		sql = "SELECT #{base_table}.id FROM #{base_table} ORDER BY #{query}"
	end
	begin
		cols = PgQueryExtension.setup(PgQuery.parse(sql)).get_all_columns
		return cols.map{ |x| QueryColumn.new(x[:table].nil? ? base_table : tablename_singularize(x[:table]), x[:column]) }
	rescue => error
		# puts "QUERY \"#{sql}\" CANNOT PARSE! orig sql = #{query}"
		# puts error
	end
	[]
end

# try to parse the complete query after collecting all sql components and get all the missing columns
def post_process_sql_string(sql, base_table)
	base_table = tablename_pluralize(base_table)
	puts("sql1 : #{sql}")
	sql = "SELECT #{base_table}.id FROM #{base_table} #{sql}"
	puts("sql2 : #{sql}")
	begin
		cols = PgQueryExtension.setup(PgQuery.parse(sql)).get_all_columns
		return cols.map{ |x| QueryColumn.new(x[:table].nil? ? base_table : tablename_singularize(x[:table]), x[:column]) }
	rescue => error
		# puts "-------"
		# puts "QUERY \"#{sql}\" CANNOT PARSE! orig sql = #{sql}"
		# puts error
		# puts "-------\n"
	end
	[]
end

# it's messy :( but here I need to set up the table correctly, e.g., joins(:issue => :project)
def extract_fields_from_args_for_join(base_table, node)
  return [] if node == nil
	output = []
	associations = find_table_in_schema(base_table).associations
	table = base_table
  if node.type == :list
		node.each do |child|
			next if !check_node_type(child, :assoc)
			child.each do |c|
        if c.type == :symbol_literal
          key = extract_string(c)
          if !key.nil?
						output << {:table => table, :column => key}
						assoc = associations.select { |ax| ax[:field]==key }
						if assoc.length > 0
							table = assoc[0][:class_name]
						end
          end 
        end
      end
    end
  end
  output
end

# order should be processed differently though... e.g., order(name => :asc)
def extract_fields_from_args_for_order(base_table, node)
  return [] if node == nil
	output = []
	associations = find_table_in_schema(base_table).associations
	if node.type == :list
		node.each do |child|
			next if !check_node_type(child, :assoc)
			if check_node_type(child[0], :label)
				output << {:table => base_table, :column => child[0].source.gsub(/:/,'')}
			elsif check_node_type(child[0],:symbol_literal)
				output << {:table => base_table, :column => extract_string(child[0])}
			end
    end
  end
  output
end

def is_query_predicate_func?(call_ident)
	call_ident[0].to_s.start_with?('find_by') or ["find", "where","rewhere", "where!","not"].include?(call_ident[0].to_s)
end
def is_join_func?(call_ident)
	["joins","left_outer_joins","includes","eager_load","preload", "references"].include?(call_ident[0].to_s)
end
def is_order_func?(call_ident)
	["order","reorder"].include?(call_ident[0].to_s)
end
def extract_query_string_from_list_node(call_ident, arg_node, base_table)
	preds = []
	if is_query_predicate_func?(call_ident) or call_ident[0].to_s == "build_from_defaults"
		fields = extract_fields_from_args_for_where(arg_node)
		# string lieratal #where("articles.author = ?")
		puts "arg[0] #{arg_node[0].source} #{arg_node[0].length} fields : #{fields}"
		if  [':all', ':first'].include?arg_node[0].source.to_s
			if arg_node.length > 1 and is_valid_node?(arg_node[1]) and arg_node[1].type == :list
				arg_node[1].each do |c|
					if c.type == :assoc
						key = extract_string(c[0])
						puts c[1].source
						if key == 'conditions'
							puts c[1].type
							if c[1].type == :array
								s, fields = extract_query_string_from_array_node(call_ident, c[1], base_table)
							end
						end
					end
				end
			end 
		end 
		fields.each do |field|
			puts "fields: #{field[:table]}"
			# e.g. lower(email)
			if field[:table]&.include?"("
				start_offset = field[:table].index("(")
				end_offset = field[:table].index(")")
				field[:table] = field[:table][start_offset+1...end_offset]
				if field[:table].include?"."
					field[:column] = field[:table].split(".")[-1]
					field[:table] = field[:table].split(".")[0]
				else
					field[:column] = field[:table]
					field[:table] = ""
				end
			end
			puts "fields after: #{field[:column]}"
			preds << QueryPredicate.new(QueryColumn.new(field[:table].blank? ? base_table : field[:table], field[:column]), '=', '?')
		end
		return fields.map{ |x| "#{tablename_pluralize(base_table)}.#{x[:column]}=?" }.join(' AND '), preds
	elsif is_order_func?(call_ident)
		fields = extract_fields_from_args_for_order(base_table, arg_node)
		return "", fields.map{ |x| QueryColumn.new(x[:table].blank? ? base_table : x[:table], x[:column])}
	else
		fields = extract_fields_from_args_for_join(base_table, arg_node)
		return "", fields.map{ |x| QueryColumn.new(x[:table].blank? ? base_table : x[:table], x[:column])}
	end
end

def extract_query_string_from_array_node(call_ident, arg_node, base_table)
	preds = []
	if arg_node[0].nil? or arg_node[0][0].nil?
		return "",[]
	end
	sql = ""
	if arg_node[0][0].type == :binary
		# for cases of concatenating strings using '+'
		sql = find_string_from_param(sql_query_fix(base_table, arg_node[0][0].source))
	elsif arg_node[0].type == :list
		sql = find_string_from_param(sql_query_fix(base_table, arg_node[0][0].source))
	else
		sql = find_string_from_param(sql_query_fix(base_table, arg_node[0].source))
	end
	preds = parse_partial_predicate(sql, base_table, call_ident)
	return sql, preds
end

def extract_query_string_from_binary_node(call_ident, arg_node, base_table)
	sql = find_string_from_param(sql_query_fix(base_table, arg_node.source))
	preds = parse_partial_predicate(sql, base_table, call_ident)
	return sql, preds
end

def extract_query_string_from_string_node(call_ident, arg_node, base_table)
	sql = find_first_string_in_node(arg_node)
	sql = sql_query_fix(base_table, sql)
	preds = parse_partial_predicate(sql, base_table, call_ident)
	return sql, preds
end

def extract_query_string_from_symbol_node(call_ident, arg_node, base_table)
	preds = [QueryColumn.new(base_table, arg_node.source.gsub(/:/,''))]
	# arg_node[0].each do |n|
	# 	if is_valid_node?(n) && n.type == :symbol_literal
	# 		preds << QueryColumn.new(base_table, n.source.gsub(/:/,''))
	# 	end
	# end
	return "", preds
end

# return both a string and a list of QueryPredicate 
# only process string
def extract_query_string_from_param(call_ident, node, base_table)
	return "",[] if node == nil 
	arg_nodes = []
	if is_query_predicate_func?(call_ident)
		if node.type != :arg_paren 
			arg_nodes = [node]
		else
			if node[0].type == :list
				arg_nodes = [node[0]]
				# puts "node 0 #{node[0].source}"
			else
				arg_nodes = [node[0][0]]
			end
		end
	else
		if check_node_type(node[0], :list)
			arg_nodes = node[0]
		end
	end
	sql,preds="",[]
	arg_nodes.each do |arg_node|
		next if !is_valid_node?(arg_node)
		ptype = arg_node.type
		s1,q1="",[]
		puts "PTYPE #{ptype} #{arg_node.source}"
		if ptype == :string_concat
			puts "STRING CONCAT"
			new_sql = replace(arg_node.source)
			contents = "\"" + new_sql + "\""
			puts "CONTENTS #{contents}"
			arg_node = YARD::Parser::Ruby::RubyParser.parse(contents).root[0]
			ptype = :string_literal
		end
		if ptype == :list
			s1,q1 = extract_query_string_from_list_node(call_ident, arg_node, base_table)
		elsif ptype == :array
			s1,q1 = extract_query_string_from_array_node(call_ident, arg_node, base_table)
		elsif ptype == :binary
			s1,q1 = extract_query_string_from_binary_node(call_ident, arg_node, base_table)
		elsif ptype == :string_literal || ptype == :call
			s1,q1 = extract_query_string_from_string_node(call_ident, arg_node, base_table)
		elsif ptype == :symbol_literal
			s1,q1 = extract_query_string_from_symbol_node(call_ident, arg_node, base_table)
		end
		sql += s1
		preds += q1
	end
	return sql,preds
end

def prev_contains_where(prev_state)
	prev_state[:prev_calls].any? { |x| ["where", "where!", "find", "rewhere", "find_by", "find_by_sql","not"].include?(x) }
end

# return SQL string, QueryPredicate list, and the new state
# state contains base_table (e.g., user.project returns Project), and previous calls
def extract_query_string_from_call(call_ident, arg_node, prev_state)
	base_table = prev_state[:base_table]
	prev_calls = prev_state[:prev_calls]
	node = call_ident
	function = node[0].to_s
	puts "function #{function}"
	if !is_valid_table?(base_table)
		return "",[],prev_state
	end
	associations = find_table_in_schema(base_table).associations
	table_schema = find_table_in_schema(base_table)
	if function != "find_in_state"
		str_param, components = extract_query_string_from_param(call_ident, arg_node, base_table)
	else
		str_param, components = "", []
	end
	ret_str = str_param
	
	puts "components #{components.length} #{components}"
	# where
	if ["where", "where!", "rewhere", "find_by", "find_by!", "not"].include?(function)
		ret_str = " #{prev_contains_where(prev_state) ? 'AND' : 'WHERE'} #{str_param}"
		if function == "NOT"
			ret_str = " NOT (#{ret_str})"
		end
	# find (by id)
	elsif function == "find"
		ret_str = " #{prev_contains_where(prev_state) ? 'AND' : 'WHERE'} id = ?"
		#components << QueryColumn.new(base_table, "id")
		components << QueryPredicate.new(QueryColumn.new(base_table, "id"), '=', '?')

	# find_by_sql
	elsif function == "find_by_sql"
		# concat all strings together
		ret_str = " " + str_param

	# find_by ??
	elsif function.start_with?("find_by")
		ret_str = str_param
		connect = prev_contains_where(prev_state) ? 'AND' : 'WHERE'
		if function.include?"_and_"
			function.sub!("find_by_","").split('_and_').each do |column|
				components << QueryPredicate.new(QueryColumn.new(base_table, column), '=', '?')
				ret_str += " #{connect} #{column} = ?"
				connect = 'AND'
			end
		end
		if function.include?"_or_"
			function.sub!("find_by_","").split('_or_').each do |column|
				components << QueryPredicate.new(QueryColumn.new(base_table, column), '=', '?')
				ret_str += " #{connect} #{column} = ?"
				connect = 'or'
			end
		end

	# boolean field as filter
	#elsif table_schema.
	
	# explicit join or inexplicit join via association
	elsif ["joins","left_outer_joins","includes","references", "eager_load","preload"].include?(function) or associations&.select { |ax| ax[:field]==function}.length > 0
		is_explicit_join = ["joins","left_outer_joins","includes","eager_load","preload", "references"].include?(function)
		if str_param.blank?
			columns = is_explicit_join ? get_fields_and_tables_for_query(components) : [QueryColumn.new(base_table, function)]
			ret_str = ""
			#puts "JOIN components = #{components}"
			components = []
			columns.each do |column|
				column_symb = column.column
				if !column.table.blank?
					associations = find_table_in_schema(column.table).associations
					base_table = column.table
				end
					
				assoc = associations.select { |ax| ax[:field]==column_symb or ax[:field] == column_symb.singularize.downcase }
				
				if assoc.length > 0
					singular_name = column_symb.singularize.downcase
					plural_name = column_symb.pluralize.downcase
					if singular_name == column_symb
						relation = "has_one"
					else
						relation = "has_many"
					end
					assoc = assoc[0]
					assoc_db_table = tablename_pluralize(assoc[:class_name])
					base_db_table = tablename_pluralize(base_table)
					puts "HERE #{function} #{assoc}, #{assoc_db_table}, #{base_db_table}"
					pk = ([relation].include?assoc[:rel])? "#{base_db_table}.id" : "#{assoc_db_table}.id"
					fk = ([relation].include?assoc[:rel])? "#{assoc_db_table}.#{base_db_table.singularize}_id" : "#{base_db_table}.#{assoc_db_table.singularize}_id"
					
					ret_str += " #{node[0]=='joins'? ' INNER':' LEFT OUTER'} JOIN #{assoc_db_table} ON #{pk} = #{fk}" 
					# components << QueryPredicate.new(QueryColumn.new(base_table, assoc[:rel]=="has_many"? 'id' : "#{assoc_db_table.singularize}_id"), 
					# 	'=', 
					# 	QueryColumn.new(assoc[:class_name], assoc[:rel]=="has_many"? "#{base_db_table.singularize}_id" : 'id'))
					if is_explicit_join
						if ["includes","eager_load","preload"].include?(function)
							join_meth =  'includes'
						elsif function == "references"
							join_meth = function
						elsif ["left_outer_joins"].include?(function)
							join_meth = 'left_outer_joins' 
						else
							join_meth = 'joins'
						end
						components << QueryColumn.new(base_table, assoc[:field], join_meth)
					else
						components << QueryColumn.new(base_table, assoc[:field])
						if assoc[:rel]=="has_many"
							components << QueryPredicate.new(QueryColumn.new(assoc[:class_name], "#{base_db_table.singularize}_id"), '=', '?')
						else
							components << QueryPredicate.new(QueryColumn.new(assoc[:class_name], "id"), '=', '?')
						end
					end
					# if assoc[:rel] == "has_many" || assoc[:rel] == "has_and_belongs_to_many"
					# 	components << QueryColumn.new(base_table, column_symb)
					# end
				end
				#associations = find_table_in_schema(assoc[:class_name]).associations
				
				if !is_explicit_join
					base_table = assoc[:class_name]
				end
			end
		else
			ret_str = " " + str_param
		end

	# order
	elsif ['order',"reorder"].include?(function)
		symbs = []
		get_fields_and_tables_for_query(components).map{|xx| [xx.table, xx.column] }.uniq.each do |table, column_symb|
			ret_str = " ORDER BY #{table}.#{column_symb}"
			symbs << column_symb
			components << QueryColumn.new(table, column_symb, 'order')
		end
		#components << QueryColumn.new(base_table, symbs.join(', '), 'order')

	# group
	elsif ['group','groupby'].include?(function)
		symbs = []
		get_fields_and_tables_for_query(components).map{|xx| xx.column }.uniq.each do |column_symb|
			ret_str = " GROUP BY #{column_symb}"
			symbs << column_symb
		end
		components << QueryColumn.new(base_table, symbs.join(', '), 'group')

	# first
	elsif ['first','first!','exists','exists?','take','last','last!'].include?(function)
		ret_str = " LIMIT 1"
		components<< QueryComponent.new("return_limit", "1")

	# limit
	elsif ['limit'].include?(function)
		components<< QueryComponent.new("return_limit", str_param)

	# pluck
	elsif ['pluck', 'select', 'try'].include?(function)
		if str_param.blank?
			get_fields_and_tables_for_query(components).map{|xx| xx.column }.each do |column_symb|
				components << QueryColumn.new(base_table, column_symb, 'select')
			end
		else
			components << QueryColumn.new(base_table, str_param, 'select')
		end

	# field
	elsif table_schema.fields.include?(function)
		components << QueryColumn.new(base_table, function, 'select')
		puts "INCLUDED #{table_schema.fields.include?(function)} #{components}" 
	# distinct
	elsif ['distinct','uniq'].include?(function)
		components << QueryComponent.new('distinct')
	
	elsif ['compact'].include?(function)
		components << QueryPredicate.new(QueryColumn.new(base_table, 'id'), "!=", "0")
	# collect = project
	elsif ['collect'].include?(function)
		# TODO

	# scope...
	elsif find_scope(base_table, function)
		components << {:class => base_table, :meth => function}

	end
	# components.map { |x| 
	# 	if !x.is_a?(Hash)
	# 		x.ruby_meth = function 
	# 	end
	# 	x }
	
	prev_state[:base_table] = base_table
	prev_state[:prev_calls] << function
	return ret_str, components, prev_state 
end

def convert_to_query_string(node, prev_state)
	base_table = prev_state[:base_table]
	if check_node_type(node, :call) and node.length>2 and node[2].type == :ident
		sql1, components1, state = convert_to_query_string(node[0], prev_state)
		sql2, components2, state = extract_query_string_from_call(node[2], node[3], state)
		#puts "c2: \t#{components1}\t #{components2} \t#{state}"
		#puts "sql = #{sql1}, #{sql2}"
		#puts "pred = #{components1}, #{components2}"
		return sql1+sql2, components1+components2, state 
	elsif check_node_type(node, :fcall) and node.length>0 and node[0].type == :ident
		return extract_query_string_from_call(node[0], node[1], prev_state)
	end
	return "",[],prev_state
end

# some hacky stuff to change the query string
def preprocess_raw_query(raw_query)
	# 0. current_user -> user
	user_strings = [['current_user', 'CurrentUser', 'user'], ['admin_user', 'AdminUser', 'user'], ["new_post", "NewPost", 'post'],  ["fetched_post", "FetchedPost",'post'], ["time", 'Time', "CheckinTime"], ["new_child", 'Head', "Person"], ["subject", 'Head', "family"], ["head", 'Head', "Person"], ["spouse", 'Head', "Person"], ["child", 'Head', "Person"]]
	user_strings.each do |n1, n2, n3|
		if raw_query.stmt.include?n1
			raw_query.stmt.gsub!(n1, n3)
			raw_query.caller_class_lst.map!{|x| 
				x[:class].gsub!(n2,n3) 
				x 
			}
		end
	end
	# 1. #{Project.table_name} --> Project
	if raw_query.stmt.include?('#') && raw_query.stmt.include?('table_name')
		raw_query.stmt.gsub!(/\#{(\W*)(\w+).table_name}/,'\2')
	end
	# 2. Arel.sql("xxx") --> "xxx"
	if raw_query.stmt.include?('Arel.sql')
		raw_query.stmt.gsub!(/Arel.sql\(\"([^\"]+)\"\)/,'"\1"')
	end
end


def parse_one_query(raw_query)
	preprocess_raw_query(raw_query)
	begin 
    	ast = YARD::Parser::Ruby::RubyParser.parse(raw_query.stmt).root 
  	rescue  
   		return nil 
	end
	base_table = raw_query[:caller_class_lst].length==0 ? raw_query[:class]: raw_query[:caller_class_lst][0][:class]
	if !is_valid_table?(base_table)
		return nil	
	end

	query_node = extract_query(ast)
	init_state = {:base_table => base_table, :prev_calls => []}
	sql, components = convert_to_query_string(query_node, init_state)

	puts "csize1: #{components.length}"
	components += post_process_sql_string(sql, base_table)
	puts "csize2: #{components.length}"
	fields = get_fields_and_tables_for_query(components)
	puts "fields: #{fields} #{sql}"
	methods = get_all_methods(query_node)
	base_object_type = nil
  if !(base_object_type = infer_object_type(query_node))
    base_object_type = raw_query.class
	end

  has_distinct = methods.include?("distinct") 
	#has_limit = %w(find find_by first first! last last! first_or_create).any? {|method| methods.include?(method)} 
	has_limit = methods.any? {|x| %w(find find_by first first! last last! first_or_create).include?(x.to_s) || x.to_s.start_with?("find_by")}

  meta = MetaQuery2.new
	meta.raw_query = raw_query
	meta.source = raw_query.stmt
	meta.has_distinct = has_distinct
	meta.methods = methods.map{|x|x.to_s}.to_a
  	meta.has_limit = has_limit
	meta.fields = fields
	meta.components = components
	meta.table = init_state[:base_table]
	meta.sql = sql

	$query_map[raw_query] = meta

	return meta
end

def first_pass(raw_queries)
	raw_queries.each do |raw_query|
    meta = parse_one_query(raw_query) 
  end
end

def second_pass(raw_queries)
	output = []
	raw_queries.each do |raw_query|
    meta = $query_map[raw_query]
		if !meta.nil?
			resolve_scopes(meta)
			output << meta
		end
	end
	output
end

def derive_metadata_with_sql(raw_queries, scopes, schema)
	output = []
	$schema = schema
	$scopes = scopes
	first_pass(raw_queries)
	output = second_pass(raw_queries)
	puts "processed success #{output.select{|x| x.fields.length>0}.count} / total #{raw_queries.length}"
	return output
end
def dump_file2issues(files2issues)
	c = []
	files2issues.each do |k, v|
		if v.length > 0
			item = {}
			item["file"] = k
			item["issues"] = v.values.map{|issue| issue.to_s}
			c.append(item)
		end
	end
	puts JSON.pretty_generate c
	return c
end
def generate_issue(patch, loc, offset, endset, t, detailed_reason)
	position = Position.new(Point.new(loc, offset), Point.new(loc, endset))
	reason = Reason.new(t, detailed_reason)
	issue = Issue.new(reason, patch, position)
end
def print_detail_with_sql(raw_queries, scopes, schema, change={})
	metas = []
	output = []
	$schema = schema
	$scopes = scopes
	$change = change
	puts "name #{$app_name}"
	succ_cnt = 0
	qcnt = 0
	puts "====scopes===="
	puts $scopes
	outputf = File.open("query.py","w" )
	output_dics = []
	raw_queries = raw_queries.sort_by { |w| w.line }
	puts "after sort #{raw_queries.length}"
	file2issues = {} # filename => issues []
	cnt = 0
	raw_queries.each do |raw_query|
		begin
			# if raw_query[:method_name].blank? #only checks scopes
			# 	next
			# end
			cnt += 1
			puts "#####{cnt} / #{raw_queries.length} QUERY #{raw_query.stmt}##"
			filename = raw_query.filename.split($app_name.downcase)[-1]
			# initialize the filename2pos hash
			if not file2issues.include?filename
				file2issues[filename] = {}
			end
			loc = raw_query.line - 1
			old_stmt = raw_query.stmt
			meta = parse_one_query(raw_query) 
			metas << meta
			across_lines = raw_query.stmt.split("\n").length 
			across_lines = 3 if across_lines == 1
			puts "ACROSS LINE: #{across_lines}"
			base_table = clean_prefix(raw_query[:caller_class_lst].length==0 ? raw_query[:class]: raw_query[:caller_class_lst][0][:class])
			if !is_valid_table?(base_table)
				next
			end

			puts "base = #{base_table}"
			if meta.nil?
				next
			end

			if !meta.sql.blank?
				#puts "\tparsed: query = #{meta.sql}"
				puts "\tcomponents = #{(meta.fields.select{|xxx| !xxx.is_a?(Hash)}.map {|xxx| "#{xxx.table}:#{xxx.column}"}).join(', ')}"
				print_str = meta.components.select{|xxx| !xxx.is_a?(Hash)}.map{|xxx| "\t"+component_str(xxx)}.join(" \\\n")
				puts "\t #{meta.fields} components = #{print_str}"
				if meta.fields.length > 1
					succ_cnt += 1
				end

			else
				puts "\tquery cannot be handled #{meta.fields.length}"
			end
			all_lines = open(raw_query.filename).readlines
			line_content = all_lines[loc]
			puts "raw_query = #{raw_query.stmt} line: #{raw_query.line} #{line_content}\n"
									
			if meta.fields.length >= 1
				outputf << "# Q #{qcnt} : " + raw_query.stmt.split("\n").map{|xxx| "# "+xxx}.join("\n")
				outputf << "\nQuery(#{meta.table})\n" + meta.components.select{|xxx| !xxx.is_a?(Hash)}.map{|xxx| dump_component(xxx)}.select{|xxx| !xxx.blank?}.join("\n")
				outputf << "\n"
				qcnt += 1
				puts "###fields###"
				meta.fields.each do |field|
					if !field.is_a?(Hash)
						field.table = field.table.gsub("::",'')
						field.table = convert_tablename(field.table)
						model_class_name = field.table
						# find the specific schema
						t = schema.select{|x| x.class_name.class_name == model_class_name}[0]
						next unless t
						table_name = t&.table_name
						table_name ||= model_class_name.downcase.pluralize
						table_field = "#{field.table}.#{field.column}"
						puts "TF: #{table_field} #{change.length}"
						if change.length > 0
							# hanlde id case separately
							if change[:col_del].include?table_field
								puts "-ERROR: #{table_field} is DELETED"
								regex = /[^a-zA-Z_\@0-9]#{field.column}[^a-zA-Z_\@0-9]/
								matches = line_content.to_enum(:scan, regex).map  { Regexp.last_match }
								matches.each do |m|
									offset = m.offset(0)[0] + 1
									endset = m.offset(0)[1] - 1
									patch = ""
									change_type = "column delete"
									detailed_reason = "#{table_field} is DELETED"
									issue = generate_issue(patch, loc, offset, endset, change_type, detailed_reason)
									file2issues[filename][issue.position] = issue
								end
							end
							if change[:col_ren].include?table_field
								regex = /[^a-zA-Z_\@0-9]#{field.column}[^a-zA-Z_\@0-9]/
								new_column_name = change[:col_ren][table_field]
								matches = line_content.to_enum(:scan, regex).map  { Regexp.last_match }
								matches&.each do |m|
									offset = m.offset(0)[0] + 1
									endset = m.offset(0)[1] - 1
									patch = "#{new_column_name}"
									change_type = "column rename"
									detailed_reason = "#{table_field} is RENAMED TO #{new_column_name}"
									issue = generate_issue(patch, loc, offset, endset, change_type, detailed_reason)
									file2issues[filename][issue.position] = issue
								end
							end
							if change[:assoc_del]&.include?(model_class_name) and change[:assoc_del][model_class_name]&.include?field.column
								regex = /[^a-zA-Z_\@0-9]#{field.column}[^a-zA-Z_\@0-9]/
								matches = line_content.to_enum(:scan, regex).map  { Regexp.last_match }
								matches.each do |m|
									offset = m.offset(0)[0] + 1
									endset = m.offset(0)[1] - 1
									new_assciation_name = change[:assoc_del][model_class_name][field.column]
									change_type = "association delete"
									patch = ""
									detailed_reason = "#{model_class_name}.#{field.column} is DELETED"
									issue = generate_issue(patch, loc, offset, endset, change_type, detailed_reason)
									file2issues[filename][issue.position] = issue
								end
							end
							if change[:assoc_change]&.include?(model_class_name) and change[:assoc_change][model_class_name]&.include?field.column
								regex = /[^a-zA-Z_\@0-9]#{field.column}[^a-zA-Z_\@0-9]/
								for i in 0...across_lines
									line_content = all_lines[loc + i]
									matches = line_content.to_enum(:scan, regex).map  { Regexp.last_match }
									puts "===== #{line_content} #{matches}"
									matches&.each do |m|
										offset = m.offset(0)[0] + 1
										endset = m.offset(0)[1] - 1
										puts "offset, end set #{offset}, #{endset}"
										new_assciation_name = change[:assoc_change][model_class_name][field.column]
										change_type = "association type change"
										patch = "#{new_assciation_name[1][:field]}"
										detailed_reason = "#{model_class_name}.#{field.column} is CHANGED FROM #{new_assciation_name[0][:rel]} TO #{new_assciation_name[1][:rel]}"
										issue = generate_issue(patch, loc + i, offset, endset , change_type, detailed_reason)
										file2issues[filename][issue.position] = issue
									end
								end
							end
							if change[:assoc_ren].include?(model_class_name) and change[:assoc_ren][model_class_name].include?field.column
								regex = /#{field.ruby_meth}[^a-zA-Z_\@0-9]+#{field.column}[^a-zA-Z_\@0-9]/
								for i in 0...across_lines
									line_content = all_lines[loc + i]
									puts "ruby_meth #{field.ruby_meth}"
									matches = line_content.to_enum(:scan, regex).map  { Regexp.last_match }
									matches&.each do |m|
										offset = m.offset(0)[0] + 1 
										offset += field.ruby_meth.length if field.ruby_meth
										endset = m.offset(0)[1] - 1
										offset = endset - field.column.length
										new_assciation_name = change[:assoc_ren][model_class_name][field.column]
										change_type = "association rename"
										patch = "#{new_assciation_name}"
										detailed_reason = "#{model_class_name}.#{field.column} is RENAMED TO #{new_assciation_name}"
										issue = generate_issue(patch, loc + i, offset, endset, change_type, detailed_reason)
										file2issues[filename][issue.position] = issue
									end
								end
							end
							if change[:idx_del].include?field.table  
								deleted_indices = change[:idx_del][field.table].keys
								is_affected = deleted_indices.detect{|x| x.length == 1 and x.include?field.column}
								if is_affected
									regex = /[^a-zA-Z_\@0-9]#{field.column}[^a-zA-Z_\@0-9]/
									for i in 0...across_lines
										line_content = all_lines[loc + i]
										matches = line_content.to_enum(:scan, regex).map  { Regexp.last_match }
										matches&.each do |m|
											offset = m.offset(0)[0] + 1
											endset = m.offset(0)[1] - 1
											patch = ""
											change_type = "index delete"
											detailed_reason = "index on #{table_field} has been DELETED"
											issue = generate_issue(patch, loc + i, offset, endset, change_type, detailed_reason)
											file2issues[filename][issue.position] = issue
										end
									end
								end
							end
							if change[:tab_del].include?field.table
								puts "-ERROR: #{field.table} is DELETED"
							end
							if change[:tab_ren].include?field.table or change[:tab_del].include?field.table
								# find Article text
								new_class_name = ""
								new_table_name = ""
								change_type = "table delete"
								if change[:tab_ren].include?field.table
									new_class_name = change[:tab_ren][field.table]
									new_table_name = new_class_name.downcase.pluralize
									change_type = "table rename"
								end
								table_regex = /[^a-zA-Z_\@0-9]#{field.table}[^a-zA-Z_\@0-9]/
								matches = line_content.to_enum(:scan, table_regex).map  { Regexp.last_match }
								if change_type == "table delete"
									detailed_reason = "#{field.table} is DELETED"
								else
									detailed_reason = "#{field.table} is RENAMED to #{change[:tab_ren][field.table]}"
								end
								matches&.each do |m|
									offset = m.offset(0)[0] + 1
									endset = m.offset(0)[1] - 1
									patch = "#{new_class_name}"
									issue = generate_issue(patch, loc, offset, endset, change_type, detailed_reason)
									file2issues[filename][issue.position] = issue
								end
								puts "hello"
								# check cases like articles.xx
								table_regex = /[^a-zA-Z_\@0-9]#{table_name}[^a-zA-Z_\@0-9]/
								matches = line_content.to_enum(:scan, table_regex).map  { Regexp.last_match }
								matches&.each do |m|
									offset = m.offset(0)[0] + 1
									endset = m.offset(0)[1] - 1
									patch = "#{new_table_name}"
									issue = generate_issue(patch, loc, offset, endset, change_type, detailed_reason)
									file2issues[filename][issue.position] = issue
								end
							end
						end

						#puts t.fields, field.column
						if !t
							puts "t is null #{field}"
							
						end
						
						if t 
							columns = [field.column]
							if field.column&.include?','
								columns = field.column.split(",")
							end
							columns.each do |column|
								column = column.strip
								if (not t.fields.include?column) and (not t.fields.include?"#{column}_id") and (not ['id','*',''].include?column)
									# puts "field doesn't exist #{field} #{column}"
								end
							end
						end
					end
				end

			end
		rescue
		end
		# if old_stmt.start_with?("CustomEmoji.local.left_joins(:category).reorder(")
		# 	exit
		# end
	end
	json_contents = dump_file2issues(file2issues)
	puts "success: #{succ_cnt} / total #{raw_queries.length}"
	outputf.close  
	return json_contents 
end

def is_variable_char(c)
	variable_chars = (0...36).map{ |i| i.to_s 36 }
	variable_chars << "@"
	return variable_chars.include?c.downcase
end

def is_not_variable_char(c)
	return (not is_variable_char(c))
end