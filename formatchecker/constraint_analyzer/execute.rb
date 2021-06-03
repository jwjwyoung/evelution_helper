require_relative "./parse_sql.rb"
require_relative "./validate.rb"
require_relative "./parse_model_constraint.rb"
require_relative "./parse_model_metadata.rb"
require_relative "./parse_controller_file.rb"
require_relative "./parse_html_constraint.rb"
require_relative "./parse_db_constraint.rb"
require_relative "./parse_alter_query.rb"
require_relative "./read_files.rb"
require_relative "./class_class.rb"
require_relative "./helper.rb"
require_relative "./version_class.rb"
require_relative "./extract_statistics.rb"
require_relative "./ast_handler.rb"
require_relative "./traverse_db_schema.rb"
require_relative "./parse_concerns.rb"
require_relative "./check_pattern.rb"
require "optparse"
require "yard"
require "active_support"
require "active_support/inflector"
require "active_support/core_ext/string"
require "regexp-examples"
require "test/unit"
load_validate_api # load the model api
load_html_constraint_api # load the html api
require_relative '../../query_extractor/query_parser_with_sql.rb'
require "../../query_extractor/load.rb"

$read_html = false
$read_db = true
$read_constraints = true

def test_change(app_dir, commits)
    versions = commits.map{|commit| Version_class.new(app_dir, commit)}
    traverse_all_for_db_schema(app_dir, nil, versions)
end
length = ARGV.length
if length >= 1
    app_dir = ARGV[0]
end
commits = []
if length >= 3
    commits = [ARGV[1], ARGV[2]]
end
if commits.length == 0
    new_c = `cd #{app_dir} && git rev-parse HEAD`
    old_c = `cd #{app_dir} && git rev-parse HEAD^ `
    commits = [new_c, old_c]
end
puts app_dir, commits
log_filepath = app_dir + "/output.json"
`rm #{log_filepath}`
json_dump = open(log_filepath, 'w')
json_contents = test_change(app_dir, commits)
`cd #{app_dir} && git checkout -f #{commits[0]}`
json_dump.write(json_contents)
json_dump.close()
