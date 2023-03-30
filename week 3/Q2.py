import numpy as np
import matplotlib.pyplot as plt


# firt of all we have to define eng. j
j = np.complex(0, 1)

# define some functions in this program could help us soving it better and in easier way
def xprime(x, m, t):
    A = []
    # N is the number which is known  by N in signal and system world:)
    N = len(x)

    # using one for loop in another to show the calculation of sumation thing.
    for n in t:
        # define summation variable in float.
        summation = 0.0
        for k in range(-m, m+1):
            # here we calculate summation.
            summation += a_k(x, k) * np.exp(j * k * 2 * np.pi / N * n)
        A.append(summation)
        # The append() method appends an element to the end of the list.
        # the function above could append something to A. the thing which is appended there is summation
    return A
    # finally we have the correct A


def a_k(x, k):
    # N is the number which is known  by N in signal and system world:)
    N = len(x)
    summation = 0.0
    for n in range(len(x)):  # len(x) or N
        summation += x[n] * np.exp(-1 * j * k * 2 * np.pi / N * n)
    return summation / N


# The split() method splits a string into a list.
# we want to make a list to solve the problem
x = [float(x) for x in input("Please enter your range: ").split()]
N = len(x)

# here we have to define M and t which is mentioned
M = [1, 2, 5, 10, 50]
fig, ax = plt.subplots(3, 2)
t = np.arange(-1 * N, N, 1)
plt.suptitle("Question 2")

for i in range(len(M)):
    ax[i % 3][i // 3].stem(t, xprime(x, M[i], t))
    ax[i % 3][i // 3].set_title(str(M[i]))
x1 = []

for m in range(0, 2):
    for w in x:
        x1.append(w)
        # The append() method appends an element to the end of the list.

ax[2][1].stem(t, x1)
ax[2][1].set_title("x1")
plt.show()
# and in the end we can plot the result

