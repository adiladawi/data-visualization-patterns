import matplotlib.pyplot as plt
import seaborn as sns
from datos import data
import numpy as np

d=data('mtcars')
c=d.cyl
m=d.mpg

y = np.row_stack((c,m))
x = np.arange(32)

y1, y2 = c, m


fig, ax = plt.subplots()
ax.stackplot(x, y1, y2)
sns.set_style("whitegrid")
plt.title('Motor Trend Car Road Tests Mpg and Cyl')
plt.show()
