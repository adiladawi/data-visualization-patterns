import matplotlib.patches as p
import matplotlib.pyplot as plt
import pandas
import math
from datos import data

fig=plt.figure(1, figsize=(4,4))
ax = plt.subplot(111, aspect='equal')
colors=['#FF9999', 'lightskyblue','#66FF66' ]
d=data('mtcars')
ps = pandas.Series([i for i in d.gear])
counts = ps.value_counts()

x=0.05
y=0.9 
m=0
cols=1
for i in counts:	
	for j in range(i):	
		p1 = p.Circle((x, y), 0.05, fc=colors[m], edgecolor='white')
		x=x+0.1
		ax.add_patch(p1)
		cols=cols+1
		if (cols>10):
			cols=1
			x=0.05
			y=y-0.1		
	m=m+1
x=0.05
y=0.3
m=0
for i in counts.index:	
	p2 = p.Circle((x, y), 0.05, fc=colors[m], edgecolor='white')
	ax.add_patch(p2)
	plt.text(x+0.17, y-0.03, str(int(i))+" gear", ha="center", family='sans-serif', size=11, color='b' )
	x=x+0.35
	m=m+1

ax.axis('off')
plt.title("Dot Matrix by Number of Gears", color='b', family='sans-serif', size=14)
plt.show()