import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate

x=np.linspace(-2,2,11)
y=np.exp(x)
y[-2:]=y[-3]

y=0*y;y[-1]=1

xx=np.linspace(x[0],x[-1],2001)

spln=interpolate.splrep(x,y)
yy=interpolate.splev(xx,spln)
plt.clf();
plt.plot(x,y,'*')
plt.plot(xx,yy)
plt.savefig('spline_out.png')
