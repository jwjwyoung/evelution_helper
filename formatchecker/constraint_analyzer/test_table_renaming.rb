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
load_validate_api # load the model api
load_html_constraint_api # load the html api
require_relative '../../query_extractor/query_parser_with_sql.rb'
require "../../query_extractor/load.rb"
$read_html = true
$read_db = true
$read_constraints = true
app_dir = "/Users/junwenyang/Research/evolution_helper/ruby_apps/example_app"
def test_change(app_dir, commits)
    versions = commits.map{|commit| Version_class.new(app_dir, commit)}
    traverse_all_for_db_schema(app_dir, nil, versions)
end

# table renaming

commits = ["table_rename", "811fabb7b1779629f78e1b975691a382e82e32ee"]
# test_change(app_dir, commits)

# association renaming
commits = ["association_renaming", "9571281eb0afe01da3625f350b48511dbc7efcda"]
test_change(app_dir, commits)

# association deletion
commits = ["association_deletion", "9571281eb0afe01da3625f350b48511dbc7efcda"]
#test_change(app_dir, commits)