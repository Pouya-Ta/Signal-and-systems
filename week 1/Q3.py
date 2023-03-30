import numpy as np
import matplotlib.pyplot as plt
import pandas
import math


# define  libraries which we need

P = np.pi
# define pi number as P

t = np.arange(-5, 5.1, 0.1)
n = np.arange(-5, 6)
"""
here we use arange to fix these two important parameters.
in this case the first one is none discrete and we define this part like we do above.
the second part is a discrete one. we define this one a little different.

"""

r = 1
c = 2
"""
here we just define the constant numbers which we use in the second part
these vars will be used in the next part again

"""

x_a = np.cos((P / 3) * t + (P / 4))
x_b = abs(c) * np.exp(r * t)

"""
calculate x in this format and the absoulut value is important here

"""
x_a1 = np.cos((P / 3) * n + (P / 4))
x_b1 = abs(c) * np.exp(r * n)

"""
calculate x in this format and the absoulut value is important here

"""
x_a3 = abs(c) * np.exp(r * t) * np.cos((P / 3) * t + (P / 4))
x_a4 = abs(c) * np.exp(r * n) * np.cos((P / 3) * n + (P / 4))

"""
calculate x in this format and the absoulut value is important here

"""
fig, signalQ4 = plt.subplots(3, 2)

signalQ4[0][0].plot(t, x_a)
signalQ4[1][0].plot(t, x_b)
signalQ4[2][0].plot(t, x_a3)
signalQ4[0][1].stem(n, x_a1)
signalQ4[1][1].stem(n, x_b1)
signalQ4[2][1].stem(n, x_a4)

"""
stem and plot
n for discrete signals and t for none discrete signals
"""
plt.show()

"""
here we just plot the final result which we wanted to find.
"""
