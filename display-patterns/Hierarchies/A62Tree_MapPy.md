# PYTHON IMPLEMENTATION 


## Data Set

For this example it was used Data Set called mtcars (Motor Trend Car Road Tests), which comes by default in R. This data was extracted from the 1974 Motor Trend US magazine, and comprises fuel consumption and 10 aspects of automobile design and performance for 32 automobiles (1973–74 models). 

To use this data set in Python, was used a Python module called rpy2. First create a file named as datos.py and write the next code.


~~~~{.python}
from rpy2.robjects import r
from rpy2.robjects import pandas2ri

def data(name):
    return pandas2ri.ri2py(r[name])
~~~~~~~~~~~~~



Then it is necessary import the datos.py file into the proyect, which you are working.


~~~~{.python}
from datos import data
d=data('mtcars')
~~~~~~~~~~~~~





## Dependences

* **rpy2** Python interface to the R language (Gautier, 2016)[^1].
* **Matplotlib** is a python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. matplotlib can be used in python scripts, the python and ipython shell, web application servers, and six graphical user interface toolkits (Hunter, 2016)[^2].


## Code Example


### Matplotlib


~~~~{.python}
import pylab
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from datos import data


class Treemap:
    def __init__(self, tree, iter_method, size_method, color_method,
t1):
        self.ax = pylab.subplot(111,aspect='equal')
        pylab.subplots_adjust(left=0, right=1, top=1, bottom=0)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.size_method = size_method
        self.iter_method = iter_method
        self.color_method = color_method
        self.addnode(tree)

    def addnode(self, node, lower=[0,0], upper=[1,1], axis=0):
        axis = axis % 2
        self.draw_rectangle(lower, upper, node)
        self.ax.annotate("Rectangle", upper,lower, color='w',
weight='bold',
                fontsize=13, ha='left', va='bottom')
        width = upper[axis] - lower[axis]
        try:
            for child in self.iter_method(node):
                upper[axis] = lower[axis] + (width *
float(size(child))) / size(node)
                self.addnode(child, list(lower), list(upper), axis +
1)
                lower[axis] = upper[axis]

        except TypeError:
            pass

    def draw_rectangle(self, lower, upper, node):
        r = Rectangle( lower, upper[0]-lower[0], upper[1] - lower[1],
                   edgecolor='k',
                   facecolor= self.color_method(node))
        #self.ax.text(upper[1]-0.15,lower[1]+.1,"6 Cylindres",
fontsize='12', va='center')
        self.ax.add_patch(r)


if __name__ == '__main__':
    size_cache = {}
    def size(thing):
        if isinstance(thing, int):
            return thing
        if thing in size_cache:
            return size_cache[thing]
        else:
            size_cache[thing] = reduce(int.__add__, [size(x) for x in
thing])
            return size_cache[thing]

    def random_color(thing):
        return (random.random(),random.random(),random.random())

    d=data('mtcars')
    t1 = d.pivot_table( values = 'carb',index=['cyl'], columns =
['gear'], aggfunc = len)
    tree=((2,12),((4,(1,2)),(8,(1,2))))
    Treemap(tree, iter, size,   random_color, t1)
    plt.show()
~~~~~~~~~~~~~



The complete online documentation is also available at [matplotlib](http://matplotlib.org/contents.html)


### References

[^1]: Gautier, Laurent (2016). rpy2. Consultado el 09 de Febrero, 2016 en http://rpy2.bitbucket.org/
[^2]: Hunter, John (2016). matplotlib. Consultado el 13 de Febrero, 2016 en http://matplotlib.org/
