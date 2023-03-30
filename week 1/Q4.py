import numpy as np
import matplotlib.pyplot as plt
import pandas
import math

"""
first of all we have to import the libraries we're gonna use in this program

"""

P = np.pi
"""
using numpy to fine pi number

"""
t = np.arange(-5, 5.1, 0.1)
x_t = 3 * math.sin(P * t) + 3 * abs(math.cos(7 * t))
plt.plot(t, x_t, label = "normal")

for i in range(len(x_t)):
    if x_t[i] > 5:
        x_t[i] = 5
    
    elif x_t[i] < 0:
        x_t[i] = 0
    else:
        continue
        
"""
using for loop here and conditional code to fix the value of x_t

"""

plt.plot(t, x_t, label = "limited")
plt.legend()
plt.show()
"""
here we just plot these final results

"""
