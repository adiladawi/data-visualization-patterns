import matplotlib.pyplot as plt
from datos import data

d=data('mtcars')
t =d.am
s =d.gear
plt.xlim(0,1.2)
plt.plot(t,s)
plt.xlabel('Transmission (0 = automatic, 1 = manual)')
plt.ylabel('Number of forward gears')
plt.title('Motor Trend Car Road Tests')
plt.grid(True)
plt.show()
