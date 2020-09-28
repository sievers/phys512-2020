import numpy as np
from matplotlib import pyplot as plt

x=np.linspace(-np.pi,np.pi,1001)
nper=10
mysin=np.sin(nper*x)
N=np.eye(len(x))
N=N+100*np.outer(mysin,mysin)
#A=np.outer(x,y) has A_ij=x(i)*y(j)
e,v=np.linalg.eigh(N)
dat_unrot=np.sqrt(e)*np.random.randn(len(x))
dat_rot=v@dat_unrot
