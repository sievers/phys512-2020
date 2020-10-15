import numpy as np
from matplotlib import pyplot as plt

x=np.arange(1000)
tau=50
nhit=200
x_hit=np.asarray(np.floor(len(x)*np.random.rand(nhit)),dtype='int')
y_hit=np.random.rand(nhit)**2
T=0.0*x
for i in range(nhit):
    mylen=len(x)-x_hit[i]
    T[x_hit[i]:]=T[x_hit[i]:]+y_hit[i]*np.exp(-np.arange(mylen)/tau)

f=0.0*x
#f=np.pad(f,[0,len(f)])
for i in range(nhit):
    f[x_hit[i]]=f[x_hit[i]]+y_hit[i]
g=np.exp(-1.0*x/tau)
#g=np.pad(g,[0,len(g)])
T2=np.fft.irfft(np.fft.rfft(g)*np.fft.rfft(f))
T2=T2[:len(T)]

Tft=np.fft.rfft(T)
Gft=np.fft.rfft(g)
rate=np.fft.irfft(Tft/Gft)

#if there's noise, this becaomse ift(Tft/Gft)+ift(N/Gft)
