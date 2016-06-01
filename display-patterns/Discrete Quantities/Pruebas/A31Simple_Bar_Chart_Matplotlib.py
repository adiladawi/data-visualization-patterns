import matplotlib.pyplot as plt
from datos import data
import pandas

d=data('mtcars')
ps = pandas.Series([i for i in d.gear])
counts = ps.value_counts()

plt.bar(counts.index,counts,0.35, color="blue")
plt.title('Simple Bar Chart: Car Distribution ', family='serif', size=16)
plt.xlabel('Number of Gears', family= 'serif')
plt.ylabel('Frequency', family='serif')
plt.show()