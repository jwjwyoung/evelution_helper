apps = open("repo.txt").readlines.map{|x| x.strip}
apps.each do |app|
  `cd apps; git clone #{app}`
end 
