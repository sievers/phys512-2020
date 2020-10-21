import numpy as np
from matplotlib import pyplot as plt

n=1024
x=np.linspace(-10,10,n)
model=0.18/(1+(x*2)**2)


#take random white noise, FT, multiply by sqrt(k-2) to geenerate a random walk
nvec=np.random.randn(n)
nft=np.fft.rfft(nvec)
kvec=np.arange(len(nft))
kvec[0]=kvec[1]
noise_vec=1/kvec**2


noise=np.fft.irfft(np.sqrt(noise_vec)*nft) 


shift=np.int(np.random.rand(1)*n)
#y=np.random.randn(n)+np.roll(model,np.int(np.random.rand(1)*n))
y=noise+np.roll(model,shift)

yft=np.fft.rfft(y)
yft_filt=yft/noise_vec

modft=np.fft.rfft(model)
mycorr=np.fft.irfft(yft_filt*np.conj(modft))


