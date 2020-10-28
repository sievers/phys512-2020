import numpy
import time
#import matplotlib
#matplotlib.use('TkAgg')
#import matplotlib.animation as animation

from matplotlib  import pyplot as plt

class particles:
    def __init__(self,m=1.0,npart=1000,soft=0.03,G=1.0,dt=0.1):
        self.opts={}
        self.opts['soft']=soft
        self.opts['n']=npart
        self.opts['G']=G
        self.opts['dt']=dt

        self.x=numpy.random.randn(self.opts['n'])
        self.y=numpy.random.randn(self.opts['n'])
        self.m=numpy.ones(self.opts['n'])*m
        self.vx=0*self.x
        self.vy=self.vx.copy()
    def get_forces(self):
        self.fx=numpy.zeros(self.opts['n'])
        self.fy=0*self.fx
        pot=0
        for i in range(0,self.opts['n']):
            dx=self.x[i]-self.x
            dy=self.y[i]-self.y
            rsqr=dx**2+dy**2
            soft=self.opts['soft']**2
            rsqr[rsqr<soft]=soft
            rsqr=rsqr+self.opts['soft']**2
            r=numpy.sqrt(rsqr)
            r3=1.0/(r*rsqr)
            self.fx[i]=-numpy.sum(self.m*dx*r3)*self.opts['G']
            self.fy[i]=-numpy.sum(self.m*dy*r3)*self.opts['G']
            pot+=self.opts['G']*numpy.sum(self.m/r)*self.m[i]
        return -0.5*pot
    def evolve(self):
        self.x+=self.vx*self.opts['dt']
        self.y+=self.vy*self.opts['dt']
        pot=self.get_forces()
        self.vx+=self.fx*self.opts['dt']
        self.vy+=self.fy*self.opts['dt']
        kinetic=0.5*numpy.sum(self.m*(self.vx**2+self.vy**2))
        return pot,kinetic


if __name__=='__main__':
    plt.ion()
    n=2000
    oversamp=5
    part=particles(m=1.0/n,npart=n,dt=0.1/oversamp)
    plt.plot(part.x,part.y,'*')
    plt.show()
    pot=0
    kin=0
    for i in range(100):
        plt.clf()
        plt.plot(part.x,part.y,'.')
        plt.pause(0.001)
        for j in range(oversamp):
            pot_old=pot
            kin_old=kin
            pot,kin=part.evolve()
            
        print(pot+0.5*(kin+kin_old))

        
