import math
import numpy as np

phi = (math.sqrt(5) + 1) / 2 

n = np.arange(100)
a = math.sqrt(2)
a_i = math.sqrt(2) + (n -1)
x_n = (a + a_i) / 2

print (x_n)

