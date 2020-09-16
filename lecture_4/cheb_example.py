import numpy as np

def cheb_fit(fun,ord):
    x=np.linspace(-1,1,ord+1)
    y=fun(x)
    mat=np.zeros([ord+1,ord+1])
    mat[:,0]=1
    mat[:,1]=x
    for i in range(1,ord):
        mat[:,i+1]=2*x*mat[:,i]-mat[:,i-1]
    coeffs=np.linalg.inv(mat)@y
    return coeffs

fun=np.sin
coeffs=cheb_fit(fun,51)
