import numpy as  np
from matplotlib import pyplot as plt 

x=np.arange(0,101)

y=(x*9/5)+32

plt.plot(x,y,color="red",linestyle='dotted',linewidth=2)
plt.title("Temperature comparison between Celsius and Fahrenheit")
plt.xlabel("Temperature (in Celsius)")
plt.ylabel("Temperature (in Fahrenheit)")
plt.grid(True)
plt.show()