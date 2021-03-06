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
$read_html = false
$read_db = true
$read_constraints = false
$extract_constraints = false
# app_dir = "/Users/junwenyang/Research/evolution_helper/ruby_apps/example_app"
# commits = ["97efa7af416a77c44e9fd26286ae1348e671f649", "e8f32819a06ef586ecab0a3844687d90194dbfba"]
# versions = commits.map{|commit| Version_class.new(app_dir, commit)}
# traverse_all_for_db_schema(app_dir, nil, versions)

# commits = ["column_deletion", "e8f32819a06ef586ecab0a3844687d90194dbfba"]
# versions = commits.map{|commit| Version_class.new(app_dir, commit)}
# traverse_all_for_db_schema(app_dir, nil, versions)

app_dir = "/home/junwen/Research/evolution_helper/ruby_apps/onebody"
commits = ["3.4.0", "3.3.0"]
versions = commits.map{|commit| Version_class.new(app_dir, commit)}
traverse_all_for_db_schema(app_dir, nil, versions)
