import numpy as np

N=100000
x=2*np.random.rand(N)-1
y=2*np.random.rand(N)-1
rsqr=(x**2+y**2)
ind=rsqr<1
x=x[ind]
y=y[ind]
rsqr=rsqr[ind]
rr=np.sqrt(-2*np.log(rsqr)/rsqr)
xx=x*rr
yy=y*rr
