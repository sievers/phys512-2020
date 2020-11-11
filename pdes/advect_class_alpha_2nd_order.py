import numpy as np
from matplotlib import pyplot as plt

plt.ion()

n=300
f=np.zeros(n)
if False:
    x=np.arange(n)/n*2*np.pi
    f=np.sin(x)**2+1
else:
    f[n//3:(2*n//3)]=1


osamp=20
alpha=1.0/osamp
plt.ion()

for i in range(n):
    for j in range(osamp):
        f_new=np.zeros(n+2)
        f_new[1:-1]=f
        f_new[0]=f[-1]
        f_new[-1]=f[0]
        deriv=(f_new[2:]-f_new[:-2])/2
        #deriv=(f_new[1:-1]-f_new[:-2])
        f=f-alpha*deriv
        
    plt.clf()
    plt.plot(f)
    plt.show()
    plt.pause(0.001)
