import numpy as np
from matplotlib import pyplot as plt

def fun(pars,x):
    y=pars[0]*np.sinh(pars[1]*x+pars[2])+pars[3]
    return y

def chifun_sinh(pars,dat):
    x=dat[0]
    y=dat[1]
    errs=dat[2]
    pred=fun(pars,x)
    chisq=np.sum( ((y-pred)/errs)**2)
    return chisq

def run_chain(pars,chifun,data,step_size,nsamp=5000,T=1.0):
    npar=len(pars)
    chain=np.zeros([nsamp,npar])
    chivec=np.zeros(nsamp)
    chisq=chifun(pars,data)
    for i in range(nsamp):
        pars_trial=pars+np.random.randn(npar)*step_size
        chi_new=chifun(pars_trial,data)
        delta_chi=chi_new-chisq
        if np.random.rand(1)<np.exp(-0.5*delta_chi/T):
            chisq=chi_new
            pars=pars_trial
        chain[i,:]=pars
        chivec[i]=chisq
    return chain,chivec


def run_chain_corr(pars,chifun,data,corr_mat,nsamp=5000,T=1.0):
    npar=len(pars)
    chain=np.zeros([nsamp,npar])
    chivec=np.zeros(nsamp)
    chisq=chifun(pars,data)
    L=np.linalg.cholesky(corr_mat)
    for i in range(nsamp):
        pars_trial=pars+L@np.random.randn(npar)
        chi_new=chifun(pars_trial,data)
        delta_chi=chi_new-chisq
        if np.random.rand(1)<np.exp(-0.5*delta_chi/T):
            chisq=chi_new
            pars=pars_trial
        chain[i,:]=pars
        chivec[i]=chisq
    return chain,chivec


x=np.linspace(-2,2,1001)
y_true=np.sinh(1.4*x+0.2)+0.3
sig=1.0
y=y_true+np.random.randn(len(x))*sig
plt.ion()
plt.clf()
plt.plot(x,y,'*')
plt.show()

pars_guess=np.asarray([0.8,1.3,0.1,0.5])
step_size=np.asarray([0.01,0.01,0.01,0.01])
chain,chivec=run_chain(pars_guess,chifun_sinh,[x,y,sig],step_size)
pars_guess=np.median(chain,axis=0)
step_size_better=np.std(chain[chain.shape[0]//10:,:],axis=0)
chain2,chivec2=run_chain(pars_guess,chifun_sinh,[x,y,sig],step_size_better,20000)

delt=chain2.copy()
for i in range(delt.shape[1]):
    delt[:,i]=delt[:,i]-delt[:,i].mean()
#by using a covariance matrix to draw trial steps from,
#we get uncorrelated samples much, much faster than
#just taking uncorrelated trial steps
mycov=delt.T@delt/chain2.shape[0]
chain3,chivec3=run_chain_corr(pars_guess,chifun_sinh,[x,y,sig],mycov,20000)
assert(1==0)



T=4
step_size_warm=step_size_better*np.sqrt(T)
chain_warm,chivec_warm=run_chain(pars_guess,chifun_sinh,[x,y,sig],step_size_warm,20000,T=T)
chi_warm_delt=chivec_warm-np.median(chivec_warm)
wtvec=np.exp(-0.5*chi_warm_delt*(1-1/T))
#now when I calculate any sort of quantity, I need to apply this weight

print(np.std(chain2,axis=0))
print(np.std(chain_warm,axis=0))
chain_warm_scat=chain_warm.copy()
warm_means=np.zeros(chain_warm.shape[1])
chain_warm_errs=np.zeros(chain_warm.shape[1])
for i in range(chain_warm.shape[1]):
    warm_means[i]=np.sum(wtvec*chain_warm[:,i])/np.sum(wtvec)
    #subtract the mean from the warm chain so we can calculate the
    #standard deviation
    chain_warm_scat[:,i]=chain_warm_scat[:,i]-warm_means[i]
    chain_warm_errs[i]=np.sqrt(np.sum(chain_warm_scat[:,i]**2*wtvec)/np.sum(wtvec))
    #woohoo!  this matches the unwarm chain

