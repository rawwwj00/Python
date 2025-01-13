import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,100,1000)
y=(2*t**2-16*t+24)

plt.title("Velocity-Time graph in varying accelerated motion with equation v=2t^2-16t+24")
plt.plot(t,y,color='green',linewidth=2)
plt.xlabel("Time")
plt.ylabel("Velocity")
plt.grid(True)
plt.legend()

plt.show()