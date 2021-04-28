require File.join(File.expand_path(File.dirname(__FILE__)), './query_parser_with_sql.rb')

contents = 'Todo.find(:all, :conditions => ["todos.user_id = ? AND contexts.hide = ? AND (projects.state = ? OR todos.project_id IS NULL)", current_user.id, false, "active"], :order => "todos.due IS NULL, todos.due ASC, todos.created_at ASC", :include => [:project, :context, :tags])'
node = YARD::Parser::Ruby::RubyParser.parse(contents).root
puts node[0][2].type, node[0][2].source
ast = node[0][3][0]
#lists = extract_query_string_from_list_node(ast)
extract_query_string_from_list_node(node[0][2], node[0][3], 'todo')