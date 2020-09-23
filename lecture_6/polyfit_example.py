import numpy as np
from matplotlib import pyplot as plt

#let's fit d=4-2x +0.5x**2 + 13x**3+pi x**4

def get_poly_A(x,order):
    A=np.zeros([len(x),order+1])
    A[:,0]=1
    for i in range(order):
        #A[:,i]=x**(i) #OK, but not great
        A[:,i+1]=x*A[:,i]
    return A

sig=2
x=np.linspace(-1,1,1000)
coeffs=np.asarray([4,-2,0.5,13,np.pi])
y_true=coeffs[0]+coeffs[1]*x+coeffs[2]*x**2+coeffs[3]*x**3+coeffs[4]*x**4
y=y_true+sig*np.random.randn(len(x))



plt.ion()
plt.clf()
plt.plot(x,y_true)
plt.plot(x,y,'*')


A=get_poly_A(x,28)
N=sig**2*np.eye(len(x))
Ninv=np.linalg.inv(N)

#solve A^T N^-1 A m = A^T N-1 d
lhs=A.T@(Ninv@A)
rhs=A.T@(Ninv@y)
m=np.linalg.inv(lhs)@rhs

#<d>=Am
y_pred=A@m
plt.plot(x,y_pred)



l,v=np.linalg.eigh(lhs)
print('largest,smallest eigenvalues are ',l.max(),l.min())

u,s,v=np.linalg.svd(A,0)
print('svd condition is ',s.max()/np.abs(s).min())
fitp_svd=v.T@(np.diag(1/s)@(u.T@y))
y_pred_svd=A@fitp_svd
plt.plot(x,y_pred_svd)



