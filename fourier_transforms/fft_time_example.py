import numpy as np
import time

n0=1000000+334244
dn=100
x=np.random.randn(n0+dn)
for i in range(dn):
    t1=time.time()
    y=np.fft.fft(x[:n0+i])
    t2=time.time()
    print(i,t2-t1)
