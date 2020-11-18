import numpy
import numpy as np
from matplotlib import pyplot as plt


osamp=100

def update_lax(f,deriv,alpha,dt):
    rhs=(1-alpha)*f[1:-1]+0.5*alpha*f[2:]+0.5*alpha*f[:-2]
    #f[1:-1]=0.5*(f[:-2]+f[2:])+dt*deriv[1:-1]
    f[1:-1]=rhs+dt*deriv[1:-1]

class Fluid:
    def __init__(self,npix=200,gamma=5.0/3.0,bc_type='periodic'):
        self.rho=numpy.zeros(npix)
        self.p=numpy.zeros(npix)
        self.v=numpy.zeros(npix)
        self.rhoE=numpy.zeros(npix)
        self.P=numpy.zeros(npix)
        self.gradrho=numpy.zeros(npix)
        self.gradp=numpy.zeros(npix)
        self.gradrhoE=numpy.zeros(npix)
        self.gamma=gamma
        self.bc_type=bc_type
        self.n=npix
        self.dx=1.0/npix
    def ic_bullet(self):
        self.rho[:]=1.0
        self.rhoE[:]=1.0
        self.p[:]=0
        self.p[self.n//2:3*self.n//5]=1.0

    def ic_shock_tube(self):
        #set up classic Sod shock tube problem.
        self.rho[0:self.n//2]=1.0
        self.P[0:self.n//2]=1.0

        self.rho[self.n//2:]=0.125
        self.P[self.n//2:]=0.1
        self.p[:]=0
        #we really need the energy, not the pressure
        self.rhoE=1.0/(self.gamma-1.0)*self.P

    def get_velocity(self):
        #get the velocity, if density is zero, set velocity to be zero
        self.v[:]=0
        ii=self.rho>0
        self.v[ii]=self.p[ii]/self.rho[ii]
    def get_bc(self):
        if self.bc_type=='periodic':
            self.rho[0]=self.rho[-2]
            self.rho[-1]=self.rho[1]
            self.p[0]=self.p[-2]
            self.p[-1]=self.p[1]
            self.rhoE[0]=self.rhoE[-2]
            self.rhoE[-1]=self.rhoE[1]
            return
        if self.bc_type=='smooth':
            self.rho[0]=self.rho[1]
            self.rho[-1]=self.rho[-2]
            self.p[0]=self.p[1]
            self.p[-1]=self.p[-2]
            self.rhoE[0]=self.rhoE[1]
            self.rhoE[-1]=self.rhoE[-2]
            return    
        assert(1==0)  #why did we do this?  Tutorial problem 1
    def do_eos(self):
        #self.get_velocity() #let's assume velocity has already been calculated
        thermal=self.rhoE-self.rho*0.5*self.v**2
        self.P=(self.gamma-1.0)*thermal

    def get_derivs(self):
        frho=self.p
        fp=self.p*self.v #+self.P, but we'll handle pressure slightly differently
        fE=self.v*self.rhoE+self.v*self.P
        
        drho=0*self.rho
        dp=0*self.p
        drhoE=0*self.rhoE
        mask=self.v>0
        mask[0]=False
        mask[-1]=False
        mask_r=np.roll(mask,1)
        #mask_l=np.roll(mask,-1)
        drho[mask_r]+=frho[mask]
        drho[mask]-=frho[mask]
        dp[mask_r]+=fp[mask]
        dp[mask]-=fp[mask]
        drhoE[mask_r]+=fE[mask]
        drhoE[mask]-=fE[mask]
        mask=self.v<=0
        mask[0]=False
        mask[-1]=False

        mask_r=np.roll(mask,-1)
        drho[mask_r]+=frho[mask]
        drho[mask]-=frho[mask]
        dp[mask_r]+=fp[mask]
        dp[mask]-=fp[mask]
        drhoE[mask_r]+=fE[mask]
        drhoE[mask]-=fE[mask]

        #this is simple code to make the derivatives obvious
        #but is very slow without numba
        #for ii in range(1,self.n-1):            
        #    if self.v[ii]>0:
        #        drho[ii+1]+=frho[ii]
        #        drho[ii]-=frho[ii]
        #        dp[ii+1]+=fp[ii]
        #        dp[ii]-=fp[ii]
        #        drhoE[ii+1]+=fE[ii]
        #        drhoE[ii]-=fE[ii]
        #    if self.v[ii]<0:
        #        drho[ii-1]+=frho[ii]
        #        drho[ii]-=frho[ii]
        #        dp[ii-1]+=fp[ii]
        #        dp[ii]-=fp[ii]
        #        drhoE[ii-1]+=fE[ii]
        #        drhoE[ii]-=fE[ii]
        #Why is there a factor of 1/2 in the pressure gradient? Tutorial problem 2
        gradP=0.5*(self.P[2:]-self.P[0:-2])
        dp[1:-1]-=gradP
        self.gradrho=drho
        self.gradp=dp
        self.gradrhoE=drhoE
    def get_timestep(self,dt=0.1):
        #tutorial problem 3 - what should this timestep actually be from CFL?
        return 0.5*dt  #*self.dx
    def take_step(self):
        #before we can do anything else, get the boundary gonditions
        self.get_bc()
        #then, get the velocities
        self.get_velocity()
        #now calculate the pressure
        self.do_eos()
        #now we can get the derivatives
        self.get_derivs()
        
        #find out our timestep
        dt=self.get_timestep()/osamp
        
        #and update quantities
        self.rho+=self.gradrho*dt
        self.p+=self.gradp*dt
        self.rhoE+=self.gradrhoE*dt
    def take_step_class(self,dt=0.1):
        self.get_bc()
        self.get_velocity()
        self.do_eos()
        self.get_derivs()
        dt=self.get_timestep()/osamp

        #self.rho=self.rho+dt*self.gradrho
        #self.p=self.p+dt*self.gradp
        #self.rhoE=self.rhoE+dt*self.gradrhoE
        alpha=0.01/osamp
        update_lax(self.rho,self.gradrho,alpha,dt)
        update_lax(self.p,self.gradp,alpha,dt)
        update_lax(self.rhoE,self.gradrhoE,alpha,dt)


if __name__=='__main__':
    plt.ion()
    fluid=Fluid(npix=500,bc_type='smooth')
    

    #fluid.ic_bullet()
    #plt.plot(fluid.p)

    fluid.ic_shock_tube()
    #fluid.ic_bullet()
    plt.plot(fluid.rho)
    plt.draw()
    fluid.take_step()


    plt.clf()
    h,=plt.plot(fluid.rho)
    plt.axis([0,len(fluid.rho),0,1.2])
    plt.pause(0.01)

    for i in range(0,3000):
        for i in range(osamp):
            fluid.take_step_class()
        #plt.clf()
        #plt.plot(fluid.rho)
        #plt.axis([0,len(fluid.rho),0,1.2])
        h.set_ydata(fluid.rho)
        plt.pause(0.001)
