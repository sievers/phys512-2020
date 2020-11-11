import numpy as np
from matplotlib import pyplot as plt

n=300

x_i=np.arange(n)
m_i=np.zeros(n)
m_i[n//3:(2*n)//3]=1

alpha=1.0
x=x_i.copy()


plt.clf();
for i in range(n):
    x=x+alpha
    plt.clf()
    plt.plot(x,m_i)
    plt.show()
    plt.pause(0.001)
