import numpy as np
from matplotlib import pyplot as plt

plt.ion()

n=128

bc=np.zeros([n,n])
mask=np.zeros([n,n],dtype='bool')
V=np.zeros([n,n])

x=np.linspace(-1,1,n)
xx,yy=np.meshgrid(x,x)
rsqr=xx**2+yy**2
eps=0.1
mask[rsqr<eps**2]=True
bc[rsqr<eps**2]=1.0

mask[:,0]=True
mask[:,-1]=True
mask[0,:]=True
mask[-1,:]=True

for i in range(n*10):
    ave=(np.roll(V,1,axis=0)+np.roll(V,-1,axis=0)+np.roll(V,1,axis=1)+np.roll(V,-1,axis=1))/4
    V=ave
    V[mask]=bc[mask]
    plt.clf();
    plt.imshow(V)
    plt.pause(0.001)
