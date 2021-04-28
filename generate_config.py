# run the first time to use the tool, to generate the config file for rails_best_practices, ruby_apps, and app_dir
import os
cwd = os.getcwd()
print(cwd)
file = open("query_extractor/config.yml", 'w')
file.write("apps_dir: {}/ruby_apps/\n".format(cwd))
file.write("constraint_analyzer_dir: {}/constraint_analyzer/\n".format(cwd))
file.write("tmp_output_dir: {}/tmp/\n".format(cwd))
file.write("rails_best_practices_cmd: {}/rails_best_practices/bin/rails_best_practices\n".format(cwd))
file.close()
