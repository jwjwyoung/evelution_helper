require 'active_support/all'
app = ARGV[0]
v1 = ARGV[1]
v2 = ARGV[2]
cnt = `cd #{app} && git rev-list --ancestry-path #{v1}..#{v2} | wc -l`
t1 = `cd #{app} &&  git log #{v1}  | grep Date | head -1`.split("Date:")[-1].strip
t2 = `cd #{app} &&  git log #{v2}  | grep Date | head -1`.split("Date:")[-1].strip
puts "#{t1}, #{t2}"
t1 = t1.to_datetime
t2 = t2.to_datetime
tag1 = `cd #{app} && git describe --contains #{v1}`
tag2 = `cd #{app} && git describe --contains #{v2}`
hours = (t2.to_time - t1.to_time) / 1.hours
puts "tag1: #{tag1} tag2: #{tag2}"
puts cnt, hours

