import numpy as np
from matplotlib import pyplot as plt

x=np.random.randn(1000)
#for a random walk, each step starts from where the last one took place
x=np.cumsum(x)
xft=np.fft.rfft(x)
plt.ion()
plt.clf()
plt.plot(np.abs(xft)**2)


#now do a random walk in Fourier space, using 1/k for the amplitude
#because power spectrum is 1/k^2
n=500
xft=np.random.randn(n)+1J*np.random.randn(n)
xft[0]=0
k=np.arange(n)
scale_vec=1/k
#scale_vec=1/k**(4/3)  #4/3 for 2D kolmogorov
#ps=(1+(k/k[5])**-8/3) #kolmogorov plus white noise
#scale_vec=np.sqrt(ps)
scale_vec[0]=0
xx=np.fft.irfft(xft*scale_vec)
