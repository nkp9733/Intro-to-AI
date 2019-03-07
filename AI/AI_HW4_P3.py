import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, exp, pi
import random as rand


def cumulative_dist_func(N):
    x = []
    phi = []
    count = 0
    while count<N:
        num = rand.uniform(-5,6)
        x.append(num)
        count+=1

    for i in range(0,len(x)):
        val = 0.5 + (0.5*np.sign(x[i]))*(sqrt(1-(exp(-2*(x[i]**2)/pi))))
        phi.append(val)
    print phi
    return phi

phi = cumulative_dist_func(1000)
n, bins, patches = plt.hist(phi, 50) 
plt.xlabel('Phi(x)')
plt.ylabel('Count')
plt.title(r'CDF: N=1000')
plt.axis([-5, 5, 0, 400])
plt.grid(True)
plt.show()
    
