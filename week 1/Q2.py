import numpy as np
import matplotlib.pyplot as plt
import pandas
import math

"""
first of all we have to import the libraries we're gonna use in this program
in this question we wanna show every signal contains an odd and an even value

"""


n = np.array([i for i in input("enter n : ").strip().split()], int)
x = np.array([i for i in input("enter x : ").strip().split()], int)
"""
here we wanted to use array but we know we do not have this ability in python so we just use numpy here

"""

even = ((x + np.flip(x)) / 2)
odd = ((x - np.flip(x)) / 2)
"""
even and odd in signals which we learned before.
as i said in this question we wanna show every signal contains an odd and an even value
so we do it with define the value odd and even
"""

fig, SignalQ3 = plt.subplots(3, 1)
SignalQ3[0].stem(n, x)
SignalQ3[1].stem(n, even)
SignalQ3[2].stem(n, odd)
"""
just like the code in  HW2 here we set these up. 

"""

plt.show()
"""
by this function we can plot what we need.

"""
