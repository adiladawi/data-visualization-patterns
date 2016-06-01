from datos import data
import matplotlib.pyplot as plt

d=data('mtcars')

carb=d.carb
wt= d.wt

plt.ylim(0,11)
plt.title('Motor Trend Car Road Tests Carb and wt')
plt.plot(carb , '--',wt, '--')
plt.show()

