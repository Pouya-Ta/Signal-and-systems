import numpy as np
import matplotlib as plt
import pandas
import math
"""
first of all we have to import the libraries we're gonna use in this program

"""

j = np.complex(0, 1)
P = np.pi
"""
define the pi number and the variable
we used numpy here for pi number and using complex
"""
xa_t1 = np.arange(0, 5, 0.1)
xa_n1 = np.arange(0, 5)
xb_t2 = np.arange(0, 3, 0.1)
xb_n2 = np.arange(0, 3)
xc_t3 = np.arange(0, 6, 0.1)
xc_n3 = np.arange(0, 6)
xd_t4 = np.arange(0, 5, 0.1)
xd_n4 = np.arange(0, 5)
"""
numpy arange function to define these value's range.
name them by there names in question file
"""

x1_t = np.exp(j * 3 * (xa_t1 / 7))
x1_n = np.exp(j * 3 * (xa_n1 / 7))
x2_t = abs(math.sin((2 * P) * (xb_t2 / 3))) + math.cos((4 * P) * (xb_t2 / 3))
x2_n = abs(math.sin((2 * P) * (xb_n2 / 3))) + math.cos((4 * P) * (xb_n2 / 3))
x3_t = np.exp(j * P * (xc_t3 / 3)) + np.exp(j * 4 * P * (xc_t3 / 3))
x3_n = np.exp(j * P * (xc_n3 / 3)) + np.exp(j * 4 * P * (xc_n3 / 3))
x4_t = math.sin((2 * P) * xd_t4) + math.cos(9 * xd_t4)
x4_n = math.sin((2 * P) * xd_n4) + math.cos(9 * xd_n4)
"""
here we fixed the equation which is gonna calculate the value of this variables. 
we use numpy here to use sin, cos, abs etc.
"""

fig, SignalQ2 = plt.subplots(2,2)

SignalQ2[0][0].plot(xa_t1, x1_t)
SignalQ2[0][0].stem(xa_n1, x1_n)
SignalQ2[0][1].plot(xb_t2, x2_t)
SignalQ2[0][1].stem(xb_n2, x2_n)
SignalQ2[1][0].plot(xc_t3, x3_t)
SignalQ2[1][0].stem(xc_n3, x3_n)
SignalQ2[1][1].plot(xd_t4, x4_t)
SignalQ2[1][1].stem(xd_n4, x4_n)
"""
stem and plot
n for discrete signals and t for none discrete signals
"""

plt.show()

"""
here we just plot the final result which we wanted to find.

"""

