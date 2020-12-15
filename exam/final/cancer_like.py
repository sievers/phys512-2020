import numpy
from matplotlib import pyplot as plt

def logchoose(n,m):
    #calculate some terms in the Poisson likelihood so that 
    #you don't hit numerical overflow
    v1=numpy.arange(1,m+1)
    v2=numpy.arange(n-m+1,n+1)
    logprob=numpy.log(v2).sum()-numpy.log(v1).sum()
    return logprob

def poisson(k,n,r):
    #calculate the log of the probability of observing k events in 
    #n trials, given an expected even probability of r.
    p1=numpy.log(r)*k
    p2=numpy.log(1.0-r)*(n-k)
    pp=p1+p2+logchoose(n,k)
    return pp

def cancer_prob(pp,nsamp=[90,90,90,90,90,90,90],ncancer=[0,3,3,2,0,0,3],dose=[0,1,2,4,1,2,4]):
    #given cancer incidence data and a model, calculate the log of the probability
    #of observing the given incidence data.
    tot_prob=0;
    for ii in range(len(nsamp)):
        tot_prob=tot_prob+poisson(ncancer[ii],nsamp[ii],pp[0]+pp[1]*dose[ii])
    return tot_prob

if __name__=='__main__':

    if (True):
        #glioma without old controls
        nsamp=[90,90,90,90,90,90,90]
        ncancer=[0,3,3,2,0,0,3]
        dose=[0,1,2,4,1,2,4]
        tag='glioma'

    if (False):
        #glioma with old controls
        nsamp=[90,90,90,90,90,90,90,550]
        ncancer=[0,3,3,2,0,0,3,11]
        dose=[0,1,2,4,1,2,4,0]
        tag='glioma_wold'

    if (False):
        #all schwannomas in males, old control
        nsamp=[90,90,90,90,90,90,90,699]
        ncancer=[0,2,1,5,2,3,6,9]
        dose=[0,1,2,4,1,2,4,0]
        tag='schwannoma_wold'

    if (True):
        #all schwannomas in males, no old control
        nsamp=[90,90,90,90,90,90]
        ncancer=[0,2,1,5,2,3,6]
        dose=[0,1,2,4,1,2,4]
        tag='schwannoma'


    guess=[0.02,0.001]
    ans=cancer_prob(guess,nsamp,ncancer,dose)
    print('log likelihood for ',guess,' is ',ans)
    
