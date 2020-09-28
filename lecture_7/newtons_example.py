import numpy as np

def f(x,params):
    #y=ax^alpha+b
    #dy/da=x^alpha
    #dy/dalpha=ax^alpha=ae^log(x)*alpha)
    #dy/dalpha=a*log(x)e^log(x)*alpha=a*log(x)*x^alpha
    #dy/db=1
    
    a=params[0]
    alpha=params[1]
    b=params[2]
    
    xvec=x**alpha
    y=a*xvec+b
    derivs=np.zeros([len(x),len(params)])
    derivs[:,0]=xvec
    derivs[:,1]=a*xvec*np.log(x)
    derivs[:,2]=1
    return y,derivs


x=np.linspace(1,10,1801)
a=1
alpha=-1
beta=0.5
pars=np.asarray([a,alpha,beta])
y_true,crap=f(x,pars)
sig=0.2
y=y_true+sig*np.random.randn(len(x))
N=np.eye(len(x))*sig**2
Ninv=np.eye(len(x))/sig**2

pars_guess=np.asarray([1.2,-0.8,0.3])*100
pars_cur=pars_guess.copy()
for iter in range(10):
    y_pred,derivs=f(x,pars_cur)
    resid=y-y_pred #data minus current model
    rhs=derivs.T@(Ninv@resid)
    lhs=derivs.T@Ninv@derivs
    step=np.linalg.inv(lhs)@rhs
    pars_cur=pars_cur+step
    print('iteration ',iter,' has step ',step)
par_errs=np.sqrt(np.diag(np.linalg.inv(lhs)))
print('final parameters are ',pars_cur,' with errors ',par_errs)
