import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
data1 = """1	spree	remove distinct	1.027027027	342	psql
2	redmine	remove distinct	2.063	315.7	psql
3	redmine	remove distinct	1.692	293.24	psql
4	redmine	remove distinct	1.66	272.67	psql
5	spree	remove distinct	1.19	105.53	psql
6	discourse	remove distinct	1.5	72	psql
7	spree	remove distinct	1.07	0.66	psql
8	spree	remove distinct	1.06	0.66	psql"""

data1 = data1.split("\n")



def draw(data, title, suffix2='comp'):
  value_range = [0, 5]
  legends = []
  fig, ax = plt.subplots()

  right_side = ax.spines["right"]
  right_side.set_visible(False)
  upper_side = ax.spines["top"]
  upper_side.set_visible(False)
  xaxis = [d[0] for d in data]
  speedup = [d[3] for d in data]
  querytime = [d[4] for d in data]
  category = "query time"
  # '-', 'o', '#4d8bf4'
  ls = '-'
  m = 'o'
  color = '#4d8bf4'
  l, = plt.plot(xaxis, querytime,  label=category, linestyle=ls, color=color)
  if len(m) > 0:
      l1 = plt.scatter(xaxis, querytime, marker=m, color=color)
  legend = mlines.Line2D([], [], color=color, marker=m,  linestyle=ls,
                        markersize=6, label=category)
  legends.append(legend)

  lg = plt.legend(handles=legends, bbox_to_anchor=(0, 1.2), ncol=2, loc='upper left', prop={'size': 12},frameon=False)
  plt.xlabel('Query Number', fontsize=12)  
  plt.ylabel("Query Time", fontsize=12)  
  for label in (ax.get_xticklabels() + ax.get_yticklabels()):
    label.set_fontsize(12)
  # plt.xticks(x, xx)
  plt.ylim(value_range)
  fn = '{}-{}.pdf'.format(title.lower(), suffix2)
  print("fn ", fn)
  plt.savefig(fn, 
  bbox_extra_artists=(lg,),
  bbox_inches='tight')  

data1 = [d.split("	") for d in data1]
print(data1)
title = data1[0][2]
draw(data1, title)