import seaborn as sns
import matplotlib.pyplot as plt
from datos import data
import pandas

d=data('mtcars')
ps = pandas.Series([i for i in d.gear])
counts = ps.value_counts()

sns.set(style="white", context="talk")

f, (ax1) = plt.subplots()
sns.barplot(counts.index, counts, palette="BuGn_d")
ax1.set_title("Simple Bar Chart: Car Distribution")
ax1.set_ylabel("Frequency")
ax1.set_xlabel("Number of Gears")
plt.show()