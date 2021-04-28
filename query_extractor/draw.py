import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as ticker
import matplotlib.ticker as tick

data1 = """1	spree	remove distinct	1.027027027	342	psql
2	redmine	remove distinct	2.063	315.7	psql
3	redmine	remove distinct	1.692	293.24	psql
4	redmine	remove distinct	1.66	272.67	psql
5	spree	remove distinct	1.19	105.53	psql
6	discourse	remove distinct	1.5	72	psql
7	spree	remove distinct	1.07	0.66	psql
8	spree	remove distinct	1.06	0.66	psql"""

data2 = '''fz	spree	str precheck	1.576255708	172.6	psql
31	spree	str precheck	1.256267137	128.29	psql
32	onebody	str precheck	2.5	91.13	psql
33	onebody	str precheck	2.48	55.58	psql
34	spree	str precheck	5.06	39.26	psql
35	onebody	str precheck	1.62	21.76	psql
36	onebody	str precheck	2.31	20.57	psql
37	onebody	str precheck	2.31	20.35	psql'''

data3 = '''9	redmine	remove join	1.538	290.3	psql	
10	redmine	remove join	1.437	260.12	psql	
11	onebody	remove join	5	87.35	psql	8
12	discourse	remove join	1.596685083	28.9	psql	
13	spree	remove join	1.48	0.5	psql'''




def draw(data, title, suffix2='comp', data2={}):
  value_range = [0, 1000]
  legends = []
  fig, ax = plt.subplots()
  ax2 = ax.twinx()
  right_side = ax.spines["right"]
  right_side.set_visible(False)
  upper_side = ax.spines["top"]
  upper_side.set_visible(False)
  xaxis = [d[0] for d in data]
  x_indices = sorted(enumerate(xaxis), key = lambda v: int(v[1]))
  x_indices = [v[0] for v in x_indices]
  #xaxis = ["q" + str(xaxis[i]) for i in x_indices]

  data = [data[i] for i in x_indices]
  speedup = [float(d[3]) for d in data]

  fig.set_size_inches(12 * len(speedup) / 8, 6)
  querytime = [float(d[4]) for d in data]

  # speedup = [speedup[i] for i in x_indices]
  # querytime = [querytime[i] for i in x_indices]
  category = "Query Time"
  # '-', 'o', '#4d8bf4'
  ls = '--'
  m = 'o'
  color1 = '#4d8bf4'
  color = '#fabc0a'
  c = '#eb4a3b'
  if title == 'add limit':
    color1 = color
  fz = 18
  # ax.bar(xaxis, speedup, color=color1, width=0.8)
  new_axis = xaxis + [0 for i in range(8 - len(xaxis))]
  for i, x in enumerate(new_axis):
    if i < len(speedup):
      sp = speedup[i]
      ax.bar(i-0.2,  sp, color=color1, width=0.4)
      if int(x) in data2:
        sp2 = float(data2[int(x)][3])
        ax.bar(i + 0.2, sp2, color=color, width=0.4)
    else:
      ax.bar(i-0.2, 0)

  ax.set_ylabel('Speed Up', fontsize=fz)  
  ax.set_xlabel('Query Number', fontsize=fz)  


  q2 = [[i, float(data2[int(x)][4])] for i, x in enumerate(xaxis) if int(x) in data2]
  print(q2)
  l, = ax2.plot([q[0] + 0.2 for q in q2], [q[1] for q in q2],  label=category, linestyle=ls, color=c)
  ax2.scatter([q[0] + 0.2 for q in q2], [q[1] for q in q2], marker='*', color=c,s=200)


  l, = ax2.plot([i - 0.2 for i in range(len(xaxis))], querytime,  label=category, linestyle=ls, color=c)
  if len(m) > 0:
      l1 = ax2.scatter([i - 0.2 for i in range(len(xaxis))], querytime, marker=m, color=c,s=200)
  if title != 'add limit':
    legends.append(plt.Rectangle((0,0),1,1, color=color1, label='Psql Speed Up')) 
  legends.append(plt.Rectangle((0,0),1,1, color=color, label='Mysql Speed Up'))

  legend = mlines.Line2D([], [], color=c, marker=m,  linestyle=ls,
                        markersize=10, label='Psql Query Time')
  if title != 'add limit':
    legends.append(legend)
  legend = mlines.Line2D([], [], color=c, marker='*',  linestyle=ls,
                        markersize=10, label='Mysql Query Time')
  legends.append(legend)
#   legend = mlines.Line2D([], [], color=color1, marker=m,  linestyle=ls,
#                         markersize=6, label=category)
#   legends.append(legend)
  
  # def y_fmt(x):
  #   return 'q{}'.format(x)

  lg = plt.legend(handles=legends, bbox_to_anchor=(0, 1.35), ncol=2, loc='upper left', prop={'size': fz},frameon=False)
  plt.xlabel('Query Number', fontsize=fz)  
  ax2.set_ylabel("Query Time", fontsize=fz)  
  ax2.set_ylim([0.1, 1000])
  ax.set_ylim([0, 5])
  
#   ax2.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: '{:g}'.format(y)))

  ax2.set_yscale('log')
  for label in (ax.get_xticklabels() + ax.get_yticklabels()):
    label.set_fontsize(fz)
  for label in (ax2.get_xticklabels() + ax2.get_yticklabels()):
    label.set_fontsize(fz)

  # plt.xticks(x, xx)
  va = 'top'
  space = -1
  ax.set_xlim(-1,len(speedup))
  ax2.set_xlim(-1,len(speedup))
  lbs = ['']
  lbs += ['q' + str(x) for x in xaxis]

  ax.set_xticklabels(labels=lbs)
  plt.xlabel("Query Number", fontsize=fz)
#   for index, v in enumerate(speedup):
  for index, rect in enumerate(ax.patches):
    i = index // 2

    if index%2 == 0 and i < len(data) and len(data[i]) >= 7:
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2
        
        label = "{}X".format(int(data[i][6]))
        print(y_value, label, x_value)
        ax.annotate(
        label,                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(0, space),          # Vertically shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        ha='center',                # Horizontally center label
        va=va,
        color='black',
        fontsize=fz)                      # Vertically align label differently for
                                        # positive and negative values.
 
    if index%2 != 0 and i < len(data):
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2
        print("x_value ", x_value)
        x = int(data[i][0])
        if x in data2 and len(data2[x]) > 7:
          label = "{}X".format(int(data2[x][7]))
          print(y_value, label, x_value)
          ax.annotate(
          label,                      # Use `label` as label
          (x_value, y_value),         # Place label at end of the bar
          xytext=(0, space),          # Vertically shift label by `space`
          textcoords="offset points", # Interpret `xytext` as offset in points
          ha='center',                # Horizontally center label
          va=va,
          color='black',
          fontsize=fz)                      # Vertically align label differently for
                                          # positive and negative values.                                   
  fn = 'figures/{}-{}.pdf'.format(data[0][5], title.lower().replace(" ","-"))
  print("fn ", fn)
  plt.savefig(fn, 
  bbox_extra_artists=(lg,),
  bbox_inches='tight')  

all_data = open("data.txt").readlines()
indices = [i for i in range(len(all_data)) if all_data[i] == '\n']
datas = {}
for i, index in enumerate(indices):
  if i == 0:
      data = all_data[:index]
  else:
      data = all_data[indices[i-1] + 1: index]
  data = [d.strip() for d in data]
  print(data)
# print(indices);exit()
  data = [d.split("\t") for d in data]
  for d in data:
      print(d)
  title = data[0][2]
  if title not in datas:
    datas[title] = []
  datas[title].append(data)
for title, ds in datas.items():
  mysql_data = {int(d[0]): d for d in ds[1]}
  if title == 'add limit':
    mysql_data = {}
    ds[0] = ds[1]
  draw(ds[0], title, 'comp', mysql_data)