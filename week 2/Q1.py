import numpy as np
import pandas
import matplotlib.pyplot as plt

pi = np.pi
e = np.e
w = np.complex(0, 1)

# define signal generator here as s_generator and define it to generate what we need in this Q.
def s_generator(t):
    x=[]
    for i in t:
        if i <= 5 and i >= 4:
            x.append(1)
        elif i <= 2 and i >= 1:
            x.append(-1)
        else:
            x.append(0)
    return x

# define fourier calculator as f_calculator here and calculate fourier series.
def f_calculater(k):
    if k == 0:
        return 0
    x1 = np.exp(-4 * w * k * pi / 6)
    x2 = -np.exp(-2 * w * k * pi / 6)
    x3 = -np.exp(-10 * w * k * pi / 6)
    x4 = np.exp(-8 * w * k * pi / 6)
    x5 = 2 * w * k * pi
    return (x1 + x2 + x3 + x4) / x5

# we wanna "estimate" the signal and  we can see how to solve it in the following code
def takhmine_s(c, t):
    result = 0
    for k in range(-c, c + 1):
        result += f_calculater(k) * (np.exp(2 * w * k * pi * t / 6))

    return result

fig, axis = plt.subplots(3, 2)
plt.suptitle("x(t)")
# we have range of M here
M = [1, 2, 5, 10, 50]
t = np.arange(-3.000, 3.001, 0.001)
x = s_generator(t)
m = len(M)

for i in range(m):
    q1 = i % 3
    q2 = i // 3
    x = takhmine_s(M[i], t)
    axis[q1, q2].plot(t, x)
    axis[q1, q2].title.set_text("m = " + str(M[i]))
x = s_generator(t)
axis[2, 1].plot(t, x)
axis[2, 1].title.set_text("real x")

plt.show()
