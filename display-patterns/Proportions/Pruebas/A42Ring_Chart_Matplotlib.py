library(ggplot2)
t<-table(mtcars$cyl)
x<-as.data.frame(t)
colnames(x)<-c("Cylindres", "Frequency")
bp <- ggplot(x, aes(x ="",y=Frequency, fill = Cylindres)) +
  geom_bar(width = 1,  stat = "identity") +labs (title="Proportion Cylindres in a Car Distribution")
pie <-bp+coord_polar("y", start=0)
pie +   geom_text(aes(y = Frequency/3 + c(0, cumsum(Frequency)[-length(Frequency)]), 
                      label = paste(round(Frequency/sum(Frequency) * 100), " %")), size=5)
import matplotlib.pyplot as plt
from datos import data
import pandas 
import numpy as np

d=data('mtcars')
subset1, subset2, subset3= d[d.cyl==4], d[d.cyl==6], d[d.cyl==8]
ps = pandas.Series([i for i in subset1.gear])
c1 = ps.value_counts()
ps = pandas.Series([i for i in subset2.gear])
c2 = ps.value_counts()
ps = pandas.Series([i for i in subset3.gear])
c3 = ps.value_counts()

def pie(ax, values, **kwargs):    
    wedges, _, labels = ax.pie(values, autopct='%1.1f%%', **kwargs)
    return wedges

fig, ax = plt.subplots()
ax.axis('equal')
width = 0.35
kwargs = dict(colors=[ '#FF9999','#66FF66'], startangle=90)
outside = pie(ax, c3.sort_index(), radius=1, pctdistance=1-width/2, **kwargs)
kwargs = dict(colors=['#FF9999', 'lightskyblue','#66FF66' ], startangle=90)
inside = pie(ax, c2.sort_index(), radius=1-width, pctdistance=1 - (width/2) / (1-width), **kwargs)
center = pie(ax, c1.sort_index(), radius=1-2*width, pctdistance=1 - (width/2) / (1-width), **kwargs)
plt.setp(center+inside + outside, width=width, edgecolor='white')
ax.legend(inside[::-1], ['5 Gear', '4 Gear', '3 Gear'], frameon=False)
kwargs = dict(size=13, color='white', va='center', fontweight='bold')
ax.text(0, 0, '4 Cylindres', ha='center', bbox=dict(boxstyle='round', facecolor='coral', edgecolor='none'),**kwargs)
ax.annotate('8 Cylindres', (0, 0), xytext=(np.radians(-45), 1), bbox=dict(boxstyle='round', facecolor='green', edgecolor='none'),
            textcoords='polar', ha='left', **kwargs)
ax.annotate('6 Cylindres', (0, 0), xytext=(np.radians(-20), 0.9), bbox=dict(boxstyle='round', facecolor='blue', edgecolor='none'),
            textcoords='polar', ha='right', **kwargs)
plt.title("Gear Car's Distribution by Cylindres", size=18)
plt.show()