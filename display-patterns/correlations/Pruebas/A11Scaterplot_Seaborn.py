import matplotlib.pyplot as plt
import seaborn as sns
from datos import data

d=data('mtcars')
sns.set(style="white")
g = sns.FacetGrid(d)
g.map(plt.scatter, "wt", "mpg")
plt.title("Scatterplot by Milles per Gallon and  Car Weight", family='serif', size=16)
g.set_axis_labels("Car Weight","Milles per Gallon")
plt.show()