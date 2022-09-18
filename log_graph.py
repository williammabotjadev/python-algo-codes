# A graph representation of Logarithmic vs. Constant time 

import matplotlib.pyplot as plt 
from math import log 

x = list(range(1, 100))

lst_one = []
lst_two = []

a = 1 

plt.plot(x, [y * y for y in x ])
plt.plot(x, [(7 * y) * log(y, 2) for y in x])
plt.plot(x, [(6 * y) * log(y, 2) for y in x])
plt.show()