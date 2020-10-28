import numpy as np

class Particles:
    def __init__(self,x,v,m):
        self.x=x.copy()
        self.v=v.copy()
        try:
            self.m=m.copy()
        except:
            self.m=m
        self.f=np.empty(x.shape)
        self.n=self.x.shape[0]
    def get_forces(self):
        self.f[:]=0
        for i in range(self.n):
            for j in range(self.n):
                if i!=j:
                    dx=-self.x[i,:]+self.x[j,:]
                    drsqr=np.sum(dx**2)
                    r=np.sqrt(drsqr)
                    self.f[i,:]=self.f[i,:]+dx*self.m[j]/(r*drsqr)
    def update(self,dt):
        self.get_forces()
        self.x=self.x+dt*self.v
        self.v=self.v+dt*self.f
        
n=2
x=np.random.randn(n,2)
v=np.random.randn(n,2)*0
m=np.ones(n)
parts=Particles(x,v,m)
dt=0.1
for i in range(50):
    print('step ',i)
    print(parts.x)
    parts.update(dt)
