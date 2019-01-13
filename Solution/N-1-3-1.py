import math
import numpy as np
import matplotlib.pyplot  as plt

phi = (math.sqrt(5) + 1) / 2 

def cosech(x, n):
	sum = 0
	for i in range(1,n):
		sum += math.pow(-1 , i) / (x * x + i * i * phi * phi)
		++n
	return 2 * x * sum + 1 / x	
	

x = np.linspace(0.01, 10, 1000)
y = [cosech(i, 20) for i in x]

plt.plot(x, y)

x = np.linspace(-10, 0, 1000)
y = [cosech(i, 20) for i in x]

plt.plot(x, y)

plt.ylim(-10, 10)
plt.show()
