import matplotlib.pyplot as plt
import seaborn as sns
from datos import data

d=data('mtcars')
t =d.am
s =d.gear
sns.set_style("whitegrid")
plt.plot(t,s)
plt.xlabel('Transmission (0 = automatic, 1 = manual)')
plt.ylabel('Number of forward gears')
plt.title('Motor Trend Car Road Tests')
plt.show()
