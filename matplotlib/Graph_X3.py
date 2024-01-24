import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.1)
y = x ** 3

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('x^3')
plt.title('Graph of x^3')
plt.grid(True)
plt.savefig("Graph_X3.png")