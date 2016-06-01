import numpy as np
import matplotlib.pyplot as plt
from datos import data

d=data('mtcars')
t1 = d.pivot_table( values = 'carb',index=['cyl'], columns = ['gear'], aggfunc = len)
bar_width = 0.15
opacity = 0.4
rects1 = plt.bar(t1.columns, t1.values[0], bar_width, alpha=opacity,color='g')
rects2 = plt.bar(t1.columns + bar_width, t1.values[1], bar_width, alpha=opacity, color='r')
rects3 = plt.bar(t1.columns +2* bar_width, t1.values[2], bar_width, alpha=opacity, color='y')
plt.xlabel('Number of Gears')
plt.ylabel('Frequency')
plt.title('Car Distribution by Gear and Cylindres')
plt.legend(t1.index, title='Cylindres')
plt.show()