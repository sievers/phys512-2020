import numpy as np
from matplotlib import pyplot as plt

n=1024
x=np.linspace(-10,10,n)
model=5/(1+(x*10)**2)
y=np.random.randn(n)+np.roll(model,np.int(np.random.rand(1)*n))


yft=np.fft.rfft(y)
modft=np.fft.rfft(model)
mycorr=np.fft.irfft(yft*np.conj(modft))
