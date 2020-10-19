import numpy as np
N=1024
x=np.arange(N)
k=15.4
y=np.cos(2*np.pi*x*k/N)
yft=np.fft.fft(y)

xx=np.linspace(0,1,N)*2*np.pi
win=0.5-0.5*np.cos(xx)

