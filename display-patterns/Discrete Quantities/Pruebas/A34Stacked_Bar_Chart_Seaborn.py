import seaborn as sns
import matplotlib.pyplot as plt
from datos import data
import pandas

sns.set(style="whitegrid")
f, ax = plt.subplots(figsize=(6, 15))
d=data('mtcars')
t1 = d.pivot_table( values = 'carb',index=['cyl'], columns = ['gear'], aggfunc = len)
bar_width = 0.4
sns.barplot(x=t1.columns, y=t1.values[0]+t1.values[1]+t1.values[2],  label="8 ", color="#2ecc71")
sns.barplot(x=t1.columns, y=t1.values[0]+t1.values[1],  label="6 ", color="salmon")
sns.barplot(x=t1.columns, y=t1.values[0],  label="4 ", color="skyblue")
ax.legend(ncol=1, loc="center right",title="Cylindres")
sns.despine(bottom=True)
plt.title('Car Distribution by Gear and Cylindres', family='Serif', size=16)
plt.show()