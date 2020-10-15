import numpy as np
import time
def myft(f):
    if len(f)==1:
        return f
    fe=f[::2]
    fo=f[1::2]
    N=len(f)
    twid=np.exp(-2J*np.pi*np.arange(N//2)/N)
    fte=myft(fe)
    fto=myft(fo)
    ft1=fte+twid*fto
    ft2=fte-twid*fto
    return np.hstack([ft1,ft2])


N=4*128**2
f=np.random.randn(N)
t1=time.time()
ft1=myft(f)
t2=time.time()
print('took ',t2-t1,' seconds to do FFT')
ft2=np.fft.fft(f)

