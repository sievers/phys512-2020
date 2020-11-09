import numpy as np
#from numba import njit
import numba as nb
import time

@nb.njit
def bm(x_in,x_out):
    n=x_in.shape[0]
    for i in nb.prange(n):
        x=2*x_in[i,0]-1
        y=2*x_in[i,1]-1
        rsqr=x**2+y**2
        if rsqr<1:
            fac=np.sqrt(-2*np.log(rsqr)/rsqr)
            x_out[i,0]=fac*x
            x_out[i,1]=fac*y
        else:
            x_out[i,0]=-999
            x_out[i,1]=-999
def myrandn(n):
    n_guess=np.int(n/2*4/np.pi)+10  #a stab at how many random numbers we'll need
    mat=np.random.rand(n_guess,2)
    out=np.empty(mat.shape)
    bm(mat,out)
    out=np.ravel(out[out[:,0]>-900,:])
    return out
        


n=100000
fwee=myrandn(n)
t1=time.time()
fwee=myrandn(n)
t2=time.time()
flub=np.random.randn(len(fwee))
t3=time.time()
print(t2-t1,t3-t2)
