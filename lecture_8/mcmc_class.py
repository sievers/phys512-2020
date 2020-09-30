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
pars_true=np.asarray([1,1,0,0])
pars=pars_true.copy()
y_true=ourfun(x,pars)
noise=0.1
y=y_true+noise*np.random.randn(len(x))
par_sigs=np.asarray([0.01,0.01,0.01,0.01])
data=[x,y,noise]
chain,chivec=run_mcmc(pars,data,par_sigs,our_chisq,nstep=20000)
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
