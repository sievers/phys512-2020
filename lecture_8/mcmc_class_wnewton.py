import numpy as np
from matplotlib import pyplot as plt

def ourfun(x,pars):
    #y=a sin(b/(x-c))+d
    y=pars[0]*np.sin(pars[1]/(x-pars[2]))+pars[3]
    return y

def our_chisq(data,pars):
    #we need a function that calculates chi^2 for us for the MCMC
    #routine to call
    x=data[0]
    y=data[1]
    noise=data[2]
    model=ourfun(x,pars)
    chisq=np.sum( (y-model)**2/noise**2)
    return chisq

def num_deriv(fun,x,pars,dpar):
    #calculate numerical derivatives of 
    #a function for use in e.g. Newton's method or LM
    derivs=np.zeros([len(x),len(pars)])
    for i in range(len(pars)):
        pars2=pars.copy()
        pars2[i]=pars2[i]+dpar[i]
        f_right=fun(x,pars2)
        pars2[i]=pars[i]-dpar[i]
        f_left=fun(x,pars2)
        derivs[:,i]=(f_right-f_left)/(2*dpar[i])
    return derivs


def run_mcmc(pars,data,par_step,chifun,nstep=5000):
    npar=len(pars)
    chain=np.zeros([nstep,npar])
    chivec=np.zeros(nstep)
    
    chi_cur=chifun(data,pars)
    for i in range(nstep):
        pars_trial=pars+np.random.randn(npar)*par_step
        chi_trial=chifun(data,pars_trial)
        #we now have chi^2 at our current location
        #and chi^2 in our trial location. decide if we take the step
        accept_prob=np.exp(-0.5*(chi_trial-chi_cur))
        if np.random.rand(1)<accept_prob: #accept the step with appropriate probability
            pars=pars_trial
            chi_cur=chi_trial
        chain[i,:]=pars
        chivec[i]=chi_cur
    return chain,chivec
        
#x=np.linspace(-5,5,5000)
x=np.linspace(0.1,5,5000)
pars_true=np.asarray([1,1,0,0],dtype='double')
pars=pars_true.copy()
y_true=ourfun(x,pars)
noise=0.1
y=y_true+noise*np.random.randn(len(x))

#run Newton's with numerical derivatives
Ninv=np.eye(len(x))/noise**2
dpar=np.ones(len(pars))*1e-2
for i in range(10):
    model=ourfun(x,pars)
    derivs=num_deriv(ourfun,x,pars,dpar)
    resid=y-model
    lhs=derivs.T@Ninv@derivs
    rhs=derivs.T@Ninv@resid
    lhs_inv=np.linalg.inv(lhs)
    step=lhs_inv@rhs
    pars=pars+step
    print(pars)
#since we have a curvature estimate from Newton's method, we can
#guess our chain sampling using that
par_sigs=np.sqrt(np.diag(lhs_inv))
data=[x,y,noise]
chain,chivec=run_mcmc(pars,data,par_sigs,our_chisq,nstep=20000)
par_sigs=np.std(chain,axis=0)
par_means=np.mean(chain,axis=0)

nchain=4
all_chains=[None]*nchain
for i in range(nchain):
    pars_start=par_means+3*par_sigs*np.random.randn(len(pars))
    chain,chivec=run_mcmc(pars_start,data,par_sigs,our_chisq,nstep=20000)
    all_chains[i]=chain



for i in range(nchain):
    for j in range(i+1,nchain):
        mean1=np.mean(all_chains[i],axis=0)
        mean2=np.mean(all_chains[j],axis=0)
        std1=np.std(all_chains[i],axis=0)
        std2=np.std(all_chains[j],axis=0)
        print('param difference in sigma is ',(mean1-mean2)/(0.5*(std1+std2)))

assert(1==0)

pars_sigs_new=np.std(chain,axis=0)
chain2,chivec2=run_mcmc(pars,data,pars_sigs_new,our_chisq,nstep=20000)
print('sigmas after first better chain are ',np.std(chain2,axis=0))
pars_sigs_new=np.std(chain2,axis=0)
pars=pars+5*np.random.randn(len(pars))*pars_sigs_new
chain2,chivec2=run_mcmc(pars,data,pars_sigs_new,our_chisq,nstep=50000)

param_errors=np.std(chain2,axis=0)
print("sigmas after second better chain are ",param_errors)
# # of sigmas our recovered parameters are off by truth is
#(chain_mean - truth)/param_errors
#this *ought* to be close to 1 on averag
parameter_nsig=(np.mean(chain2,axis=0)-pars_true)/np.std(chain2,axis=0)
print('we have parameter errors of ',parameter_nsig,' sigma')
