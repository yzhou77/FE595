# Use NumPy and MatPlotLib to graph one period of sine and cosine on the same set of axes.
# import Numpy and Matplotlib
import numpy as np
import matplotlib.pyplot as plt
# create x-axes
x = np.linspace(0, 2*np.pi, 201)
# create sine and cosine lines
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1,color="red",label="sine")
plt.plot(x, y2,color="blue",label="cosine")
# create title and legend
plt.title('Graph of sine and cosine on [0,2π]')
plt.xticks((0,np.pi/2,np.pi,np.pi*3/2,np.pi*2),('0','π/2','π','3π/2','2π'))
plt.legend()
# show the graph
plt.show()