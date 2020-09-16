from scipy import integrate
import numpy as np

sig=0.1

def fun(x):
    return 1.0+np.exp(-0.5*x**2/sig**2)/np.sqrt(2*np.pi*sig**2)

lims=[ [-25,25],[-20,30]]

for lim in lims:
    a=lim[0]
    b=lim[1]
    tot=integrate.quad(fun,a,b)
    #print(tot)
    #pred=(b-a)+np.sqrt(2*np.pi)*sig
    pred=(b-a)+1.0
    print('for lims ' + repr(lim) + ' error is ' + repr(np.abs(tot[0]-pred)) + ' vs. estimated error ' + repr(tot[1]))
