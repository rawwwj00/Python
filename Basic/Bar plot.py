# 'matplotlib' module is needed to be installed
from matplotlib import pyplot as plot
a={'Air':1,'Water':1.33,'Glass':1.5,'Diamond':2.42}

name=list(a.keys())
marks=list(a.values())

plot.barh(name,marks,color='purple')
plot.title("Refractive Index for different elements")
plot.xlabel("Refractive Index")
plot.ylabel("Elements")
plot.grid(True)
plot.show()