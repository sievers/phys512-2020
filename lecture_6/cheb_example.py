import numpy as np
from matplotlib import pyplot as plt


x=np.linspace(-1,1,1001)
y=np.exp(x)
order=50
A=np.polynomial.chebyshev.chebvander(x,order)
u,s,v=np.linalg.svd(A,0)

fitp=v.T@(np.diag(1/s)@(u.T@y))
order_use=5

y_pred_cheb=A[:,:order_use]@fitp[:order_use]

A2=A[:,:order_use]
u2,s2,v2=np.linalg.svd(A2,0)
fitp2=v2.T@(np.diag(1/s2)@(u2.T@y))
y_pred2=A2@fitp2
plt.clf();
plt.plot(x,y_pred_cheb-y)
plt.plot(x,y_pred2-y)
plt.show()
