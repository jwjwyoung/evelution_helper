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
$check_queries = true
app_dir = "/Users/junwenyang/Research/evolution_helper/ruby_apps/example_app"
def test_change(app_dir, commits)
    versions = commits.map{|commit| Version_class.new(app_dir, commit)}
    traverse_all_for_db_schema(app_dir, nil, versions)
end

# table renaming
class TestVersionClassConstraint < Test::Unit::TestCase
    def test_extract_uniquess_columns
        app_dir = "/Users/junwenyang/Research/evolution_helper/ruby_apps/example_app"
        commits = ["table_rename", "811fabb7b1779629f78e1b975691a382e82e32ee"]
        #test_change(app_dir, commits)
        # association renaming
        commits = ["association_renaming", "9571281eb0afe01da3625f350b48511dbc7efcda"]
        #test_change(app_dir, commits)

        # association deletion
        commits = ["association_deletion", "9571281eb0afe01da3625f350b48511dbc7efcda"]
        #test_change(app_dir, commits)
    end
    def test_redmine
        commits = ["0.6.0", '0.5.1']
        app_dir =  "/home/junwen/Research/evolution_helper/ruby_apps/redmine"
        test_change(app_dir, commits)
    end
    def test_redmine2
        commits = ["0.8.0", '0.7.4']
        app_dir =  "/home/junwen/Research/evolution_helper/ruby_apps/redmine"
        test_change(app_dir, commits)
    end
    def test_lobsters
        commits = ["c85e311b9e2c285471f6bd6bba60941efb70a17c", "a2288d8af9c7ff96463cb7fa9d508824c2e6f025"]
        app_dir =  "/home/junwen/Research/evolution_helper/ruby_apps/lobsters"
        test_change(app_dir, commits)
    end    
    def test_lobsters2
        commits = ["d4e9e024aa8d8aab70591a6084e8f4bc0fa030bb", "20c870b78be753cd6a2e9440326eb78701bf85fa"]
        app_dir =  "/home/junwen/Research/evolution_helper/ruby_apps/lobsters"
        test_change(app_dir, commits)
        # 1 column_rename in lobsters for 10 commits
    end

    def test_lobsters3
        commits = ["89cdf1101adf25be32232ca543822fd7a24486a9", "67fc2cc75c3df047d2d04e210058341dcdc73dc0"]
        app_dir =  "/home/junwen/Research/evolution_helper/ruby_apps/lobsters"
        test_change(app_dir, commits)
        # 2 column_rename in lobsters
    end

    def test_tracks
        # false positive caused by has_many(xxx) cannot be handled correctly
        # has_many(projects, xxx, xxx) do 
        # end
        commits = ["e92b22ea30b2ccbea46162f25d9794746d4eede2", "1c61f9cffb544471228048988a71ce6c9883b97e"]
        app_dir =  "/home/junwen/Research/evolution_helper/ruby_apps/tracks"
        test_change(app_dir, commits)
    end
    def test_tracks1
        commits = ["25682831c97e250d7a61a4f5a9d364050a23a38b", "ad0f617d7cb95528f3ac58f98503bdc2de2b7ef2"]
        app_dir =  "/home/junwen/Research/evolution_helper/ruby_apps/tracks"
        test_change(app_dir, commits)
    end
    def test_tracks2
        # RIGHT case
        # 4 column delete, Todo.done
        commits = ["c51587e4229f7dad7876ae8be33f1e8af0f5c487", "883bcb30bb3b4027375fb03185e5d11b80d622b5"]
        app_dir =  "/home/junwen/Research/evolution_helper/ruby_apps/tracks"
        test_change(app_dir, commits)
    end
    def test_tracks3
        # RIGHT case
        # 1 association rename 
        commits = ["01057af684cd926ac7719fcb615103acb98ba036", "de7b8e329d482e9504fb7c0daa0b53025fa106fa"]
        app_dir =  "/home/junwen/Research/evolution_helper/ruby_apps/tracks"
        test_change(app_dir, commits)
    end
    def test_tracks4
        # RIGHT case 
        # 3 association deletion 
        commits = ["f79c28231b4b935c0756e456bb84d59661bd4d8b", "65fe971d32fc9eb5e20099fdbe2bbc23d3272283"]
        app_dir =  "/home/junwen/Research/evolution_helper/ruby_apps/tracks"
        test_change(app_dir, commits)
    end    
    def test_ror1
        # no case false positive
        # delegate is used which mitigate the error
        commits = ["f486af5a660fd7ca345ba03e54e1354ffea6b2f2", "f9272d0ef7060ffd323e723ab3dde666f80846da"]
        app_dir =  "/home/junwen/Research/evolution_helper/ruby_apps/ror_ecommerce"
        test_change(app_dir, commits)
    end
    def test_diaspora1
        commits = ["f83b82902c7eefc2d76dea7b72ac5b9123b7063b", "173894d9262b2fa31096b542a9625cc914e636e3"]
        app_dir =  "/home/junwen/Research/evolution_helper/ruby_apps/diaspora"
        test_change(app_dir, commits)
    end
    def test_diaspora2
        commits = ["bb62a3dc612a3dd2ff85d68a600744b27c8dd230", "7042b43799b32023043c764d9f2045989a5e00e9"]
        app_dir =  "/home/junwen/Research/evolution_helper/ruby_apps/diaspora"
        test_change(app_dir, commits)
    end
    def test_diaspora3
        # all table is deleted, no schema, should not count
        commits = ["e0f583d7d3ce94b8f3a72c5de13cacc52b3864d9", "f043c9cc7e1e162734c435abe9eab0527baaf85f"]
        app_dir =  "/home/junwen/Research/evolution_helper/ruby_apps/diaspora"
        test_change(app_dir, commits)
    end
    def test_diaspora4
        # 7 column deletion
        commits = ["b9f5328d47f332348a010fe400d03f5cb16ec069", "f948120ba6bf4f084738a1cd3eda18f3b3bedbd0"]
        app_dir =  "/home/junwen/Research/evolution_helper/ruby_apps/diaspora"
        test_change(app_dir, commits)
    end    
    def test_diaspora5
        # index deletion
        commits = ["e9f6dbdffd8b9c74238e1183cff3918a487e4a89", "b7cd9d6238b7a62f0ca2e5bf940d02c491bad694"]
        app_dir =  "/home/junwen/Research/evolution_helper/ruby_apps/diaspora"
        test_change(app_dir, commits)
    end
    def test_diaspora6
         # index deletion
         commits = ["95def40c5532a130ce30dd00426d55e6028c06a2", "87d0778086c0f262ee31d5e6000345f0582cd19d"]
         app_dir =  "/home/junwen/Research/evolution_helper/ruby_apps/diaspora"
         test_change(app_dir, commits)
    end
    def test_spree2
        # index deletion
        commits = ["dc429bb3350629e73633b40c107ad3a0862f3d85", "8e02594ac94ae6adbaa021a6fe6f7362b7ef2849"]
        app_dir =  "/home/junwen/Research/evolution_helper/ruby_apps/spree"
        test_change(app_dir, commits)
   end
    def test_gitlab1
        # Jul 26 => AUG 1, takes 6 days
        # fix commit 5e3a208f58a7a887370888055da180f64b3692a3
        commits = ["e5e1c907c01b53194f77e8d8de53554ba1824e7c", "eb2d4adf38726da62f62e850d181cedf12c64c5e"]
        app_dir =  "/home/junwen/Research/evolution_helper/ruby_apps/gitlabhq"
        test_change(app_dir, commits)
    end
end