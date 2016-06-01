import matplotlib.pyplot as plt
import seaborn as sns
from datos import data
import pandas

sns.set(style="white")
d=data('mtcars')
colors = sns.husl_palette(3)
d=data('mtcars')
ps = pandas.Series([i for i in d.cyl])
c = ps.value_counts()
plt.pie(c,  labels=c.index, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)
plt.title('Car Distribution by Cylindres', size=18)
plt.show()