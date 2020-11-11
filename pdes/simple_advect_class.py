import numpy as np
from matplotlib import pyplot as plt

plt.ion()

n=300
f=np.zeros(n)
if True:
    x=np.arange(n)/n*2*np.pi
    f=np.sin(x)**2+1


alpha=1
plt.ion()

for i in range(n):
    f_new=np.zeros(n)
    f_new[1:]=f[1:]-alpha*f[1:]+alpha*f[:-1]
    f=f_new
    plt.clf()
    plt.plot(f)
    plt.show()
    plt.pause(0.001)
