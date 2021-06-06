apps = open("app_names.txt").readlines.map{|x| x.strip}
apps.each do |app|
  puts app, `cd #{app} && git log | grep Date | tail -1`
end 
