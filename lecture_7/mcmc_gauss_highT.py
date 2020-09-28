import numpy as np
from matplotlib import pyplot as plt

def gauss_chisq(pars,x,y,sig):
    pred=pars[0]*np.exp(-0.5*pars[2]**2*(x-pars[1])**2)+pars[3]
    chisq=np.sum( (pred-y)**2/sig**2)
    return chisq

x=np.linspace(-20,20,1001)
y_true=np.exp(-0.5*x**2)
sig=0.1
y=y_true+np.random.randn(len(y_true))*sig

T=1.0
pars=[1.2,-0.5,1.2,0.2]
npar=len(pars)
par_sigs=np.asarray([0.1,0.1,0.1,0.1])/4
nstep=5000
chain=np.zeros([nstep,npar])
chisq_vec=np.zeros(nstep)
chisq=gauss_chisq(pars,x,y,sig)

for i in range(nstep):
    pars_new=pars+np.random.randn(npar)*par_sigs
    chisq_new=gauss_chisq(pars_new,x,y,sig)
    delta_chisq=chisq_new-chisq
    if (np.exp(-0.5*(delta_chisq)/T)>np.random.rand(1)): #accept the step
        pars=pars_new
        chisq=chisq_new
    chisq_vec[i]=chisq
    chain[i,:]=pars

par_sigs=np.std(chain[1000:,:],axis=0)
for i in range(nstep):
    pars_new=pars+np.random.randn(npar)*par_sigs
    chisq_new=gauss_chisq(pars_new,x,y,sig)
    delta_chisq=chisq_new-chisq
    if (np.exp(-0.5*(delta_chisq)/T)>np.random.rand(1)): #accept the step
        pars=pars_new
        chisq=chisq_new
    chisq_vec[i]=chisq
    chain[i,:]=pars

T=4.0
chain_warm=0*chain;
par_sigs=np.std(chain[1000:,:],axis=0)
par_sigs_warm=par_sigs*np.sqrt(T)
chisq_vec_warm=0*chisq_vec
for i in range(nstep):
    pars_new=pars+np.random.randn(npar)*par_sigs_warm
    chisq_new=gauss_chisq(pars_new,x,y,sig)
    delta_chisq=chisq_new-chisq
    if (np.exp(-0.5*(delta_chisq)/T)>np.random.rand(1)): #accept the step
        pars=pars_new
        chisq=chisq_new
    chisq_vec_warm[i]=chisq
    chain_warm[i,:]=pars

dchi=chisq_vec_warm-np.median(chisq_vec_warm)
wtvec=np.exp(-dchi/2*(1-1/T))
pars_warm_mean=0*pars
pars_warm_errs=0*pars
bot=np.sum(wtvec)
for i in range(npar):
    top=np.sum(chain_warm[:,i]*wtvec)
    pars_warm_mean[i]=top/bot
    
    top2=np.sum((chain_warm[:,i]-pars_warm_mean[i])**2*wtvec)
    pars_warm_errs[i]=np.sqrt(top2/bot)
