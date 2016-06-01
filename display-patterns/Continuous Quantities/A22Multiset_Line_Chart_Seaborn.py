import matplotlib.pyplot as plt
import seaborn as sns
from datos import data

d=data('mtcars')
t=d.carb
s= d.wt

sns.set_style("whitegrid")
plt.plot(t,'--',s,'--')
plt.title('Motor Trend Car Road Tests Carb and wt')
plt.show()
