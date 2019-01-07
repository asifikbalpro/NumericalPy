# problem N.1.1.3
import math
import numpy as np
import matplotlib.pyplot  as plt


# no need to write data to a file
# use numpy and matplotlib
phi = (math.sqrt(5) + 1 / 2) # incorrect
phi = (math.sqrt(5) + 1) / 2  # correct
print(phi)
g = (360 / phi ** 2 )
print(g)

n = np.arange(500) 
r_n = np.sqrt(n)
theta_n = n*g 

x_n = r_n * np.cos(theta_n)
y_n = r_n * np.sin(theta_n)

plt.plot(x_n ,y_n, 's')
plt.title("sunflower pattern")
plt.show()


