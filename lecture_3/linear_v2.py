import numpy as np

fun=np.cos

x=np.linspace(0,np.pi/2,41)
y=fun(x)
dx=x[1]-x[0]
ans=(y[0]+y[-1]+2*np.sum(y[1:-1]))/2*dx
truth=1.0
print('Integral is ',ans,' with error ',ans-truth)
ans2=(y[0]+4*np.sum(y[1::2])+2*np.sum(y[2:-1:2])+y[-1])*dx/3
print('better integral is ',ans2,' with error ',ans2-truth)
xx=0.5*(x[1:]+x[:-1])  #get x points in center instead of edge
yy=fun(xx)
ans3=np.sum(yy)*dx
print('centered integral is ',ans3,' with error ',ans3-truth)

