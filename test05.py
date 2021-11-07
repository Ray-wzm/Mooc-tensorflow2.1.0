import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
plt.figure(num=3,figsize=(8,4),)
plt.plot(x,x**2)
plt.plot(x,2*x+1,color='red',linewidth=1.0,linestyle='-.')
plt.show()