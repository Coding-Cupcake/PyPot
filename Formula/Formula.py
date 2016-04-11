import numpy as np
import matplotlib.pyplot as plt
import math

def sigmoid(X):
    '''Compute the sigmoid function '''
    #d = zeros(shape=(X.shape))

    den = 1.0 + math.e ** (-1.0 * X)

    d = 1.0 / den

    return d

X = np.linspace(-5, 5, 512, endpoint=False)
C = sigmoid(X)

plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label =r'$\frac{1}{1 + e^{-z}}$')
plt.xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
plt.yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9, 1])
plt.xlim(-5, 5)
plt.ylim(0, 1)
plt.xlabel("z")
plt.ylabel("f(z)")

plt.legend(loc='upper left', prop={'size':26})
plt.plot(X, C)

plt.show()