require 'active_support/all'

apps = ['lobsters', 'tracks',  'spree', 'diaspora', 'onebody', 'gitlabhq']

def get_data(app, type='version')
    log = "../log/#{app}_change.csv"
    lines = open(log).readlines.reverse
    length = lines.length
    moreZero = lines.select{|x| (eval(x.split("\t")[-1].strip)).values.sum > 0 }.count
    puts "#{moreZero} / #{length} #{moreZero * 1.0/ length} "
    if type == 'version'
        interval = (length - 1) / 4 + 1
        indices = [interval, interval * 2, interval * 3, length]
    else
        start_time = lines[0].split("\t")[1].to_time
        end_time = lines[-1].split("\t")[1].to_time
        interval = (end_time - start_time) / 4 
        indices =  []
        index = 0
        dis = interval
        lines.each do |line|
            time = line.split("\t")[1].to_time
            if time > start_time + dis
                indices << index
                dis += interval
            end
            index += 1
        end
        indices << length
    end
    start = 0
    results = []
    puts "Q SUM AVG"
    i = 1
    indices.each do |index|
        puts "#{start} ... #{index} #{lines[start...index].length} #{(lines[index-1].split("\t")[1].to_time - lines[start].split("\t")[1].to_time ) / 1.hour}"
        sum = lines[start...index].map{|x| (eval(x.split("\t")[-1].strip)).values.sum}.sum
        # puts "#{i}th #{sum} #{sum / lines[start...index].length}"
        i += 1
        results << [sum,  lines[start...index].length, sum / lines[start...index].length]
        start = index
    end
    return results
end
def print(app)
    log = "../log/#{app}_change.csv"
    lines = open(log).readlines.reverse
    lines.each do |line|
        cells = line.split("\t")
        puts "#{cells[0]} #{eval(cells[-1]).values.sum}"
    end
end

# print('onebody')
apps.each do |app|
    puts "#{app}"
    r = get_data(app, 'time')
end
