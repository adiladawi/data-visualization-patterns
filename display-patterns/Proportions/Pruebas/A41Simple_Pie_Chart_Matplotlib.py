import matplotlib.pyplot as plt
from datos import data
import pandas

colors = ['lightcoral', 'lightskyblue','yellowgreen']
d=data('mtcars')
ps = pandas.Series([i for i in d.cyl])
c = ps.value_counts()
plt.pie(c,  labels=c.index, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)
plt.axis('equal')
plt.title('Car Distribution by Cylindres', size=18)
plt.show()