import numpy as np
import ratfit
x=np.linspace(-6,6,2001)
pdf=np.exp(-0.5*x**2)
cdf=np.cumsum(pdf)
cdf=cdf/cdf[-1]
th=np.arctan(x)

num=np.asarray([0,1,0,0])
denom=np.asarray([1,0,0])


cdf_use=cdf[len(cdf)//2:]
th_use=th[len(th)//2:]

n=5
m=5
ind=np.arange(0,len(th_use),len(th_use)//(2*(n+m)))
ind=ind[:(n+m)]
num,denom=ratfit.ratfit_exact(cdf_use[ind],th_use[ind],n,m)

mycdf=np.random.rand(10000)
mysign=mycdf<0.5
mycdf[mysign]=1-mycdf[mysign]
myth=ratfit.rateval(num,denom,mycdf)
myth[mysign]=-1*myth[mysign]
myx=np.tan(myth)

myx2=np.random.randn(len(myx))
myx.sort()
myx2.sort()
plt.clf();
plt.plot(myx)
plt.plot(myx2)

