import numpy as np
import math
def lorentzian(x):
    return 1/(1+x**2)
def gaussian(x):
    return np.exp(-0.5*x**2)


def simpsons(fun,x):
    y=fun(x)
    dx=x[1]-x[0]
    return (y[0]+y[-1]+4*np.sum(y[1::2])+2*np.sum(y[2:-1:2]))*dx/3





n=np.asarray([3,5,7,9,13],dtype='int')
area=np.zeros(len(n))

if True:
    fun=np.exp
    x0=-1;
    x1=1;
    truth=fun(x1)-fun(x0)
if False:
    fun=np.cos
    x0=0
    x1=np.pi/2
    truth=1.0
if False:
    fun=gaussian
    x1=0.5
    x0=-x1
    truth=math.erf(np.sqrt(0.5)*x1)*np.sqrt(2*np.pi)
if False:
    fun=lorentzian
    x0=-1
    x1=1
    truth=np.arctan(1)-np.arctan(-1)

#find the area using simpson's rule for each set of points we have in our list
for i in range(len(n)):
    x=np.linspace(x0,x1,n[i])
    area[i]=simpsons(fun,x)
    print('area error with ',n[i],' points is ',area[i]-truth)

#now we'll fit a polynomial in dx to the answers
#if we evaluate this polynomial with dx=0 (i.e. first coefficient)
#we have our extrapolated answer

mat=np.zeros([len(n),len(n)])
mat[:,0]=1 #the first column corresponds to the dx**0 term, which is what we want
dx=(x1-x0)/(n-1)
for i in range(1,len(n)):
    mat[:,i]=dx**(3+i) #we know Simpson's rule kills off the linear, quadratic, and cubit terms, so start at quartic
fitp=np.dot(np.linalg.inv(mat),area)
print('area in romberg extrapolation is ',fitp[0]-truth)
