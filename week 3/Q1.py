import numpy as np
import matplotlib.pyplot as plt


# firt of all we have to define eng. j
j = np.complex(0, 1)

# The split() method splits a string into a list.
# we want to make a list to solve the problem
x = [float(x) for x in input("Please enter your range: ").split()]

# using the length function by len() can help us to figure the lenght of x out.
N = len(x)

# using one for loop in another one to make this variable and use it in the final calculation
for k in range(len(x)):
    sumation = 0.0
    # define sumation as 0 in float

    for n in range(len(x)):
        # in this loop we make sumation with np. functions
        sumation += x[n] * np.exp(-1 * j * k * 2 * np.pi / N * n)

    # we use () to show index.
    print("a(" + str(k) + ") = " + str(round(sumation / N, 4)))
