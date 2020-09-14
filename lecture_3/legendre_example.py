import numpy as np
from matplotlib import pyplot as plt
def legmat(n,npt):
    assert(npt>0)
    assert(n>=0)
    
    x=np.linspace(-1,1,npt)
    mat=np.zeros([n+1,npt])
    mat[0,:]=1.0
    if (n>0):
        mat[1,:]=x
    if (n>1):
        for i in range(1,n):
            mat[i+1,:]= ((2*i+1)*x*mat[i,:]-i*mat[i-1,:])/(i+1.0)
    return mat


polys=legmat(5,1000)

plt.clf()
plt.plot(polys.transpose())
plt.savefig('legmat.png')
