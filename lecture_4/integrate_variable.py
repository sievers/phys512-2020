import numpy as np

def lorentz(x):
    return 1/(1+x**2)

def flat_gauss(x,sigma=0.2):
    return 1+np.exp(-0.5*x**2/sigma**2)/np.sqrt(2*np.pi*sigma**2)

def integrate_step(fun,x1,x2,tol):
    print('integrating from ',x1,' to ',x2)
    x=np.linspace(x1,x2,5)
    y=fun(x)
    area1=(x2-x1)*(y[0]+4*y[2]+y[4])/6
    area2=(x2-x1)*( y[0]+4*y[1]+2*y[2]+4*y[3]+y[4])/12
    myerr=np.abs(area1-area2)
    if myerr<tol:
        return area2
    else:
        xm=0.5*(x1+x2)
        a1=integrate_step(fun,x1,xm,tol/2)
        a2=integrate_step(fun,xm,x2,tol/2)
        return a1+a2

ans=integrate_step(flat_gauss,-25,15,0.001)
