import numpy as np
from matplotlib import pyplot as plt

#solve y''=-y with RK4

def f(x,y):
    dydx=np.asarray([y[1],-y[0]])
    return dydx

    #y[0]=y
    #y[1]=dy/dx
    #y'[0]=y[1]
    #y'[1]=-y[0]

def rk4(fun,x,y,h):
    k1=fun(x,y)*h
    k2=h*fun(x+h/2,y+k1/2)
    k3=h*fun(x+h/2,y+k2/2)
    k4=h*fun(x+h,y+k3)
    dy=(k1+2*k2+2*k3+k4)/6
    return y+dy

npt=201
x=np.linspace(0,np.pi,npt)
y=np.zeros([2,npt])
y[0,0]=1 #starting conditions
y[1,0]=0 #if I start at peak, then first derivative =0
for i in range(npt-1):
    h=x[i+1]-x[i]
    y[:,i+1]=rk4(f,x[i],y[:,i],h)
truth=np.cos(x)
print(np.std(truth-y[0,:]))

plt.ion()
plt.plot(x,y[0,:]-truth)
plt.title('RK4 error, ' + repr(npt)+ ' points')
plt.savefig('rk4_err.png')
