import seaborn as sns
import matplotlib.pyplot as plt
from datos import data

sns.set(style="whitegrid")
d=data('mtcars')
sns.countplot(x="gear", hue="cyl", data=d)
sns.axlabel( "Number of Gears", "Frequency")
plt.title('Car Distribution by Gear and Cylindres', family='Serif', size=16)
plt.show()