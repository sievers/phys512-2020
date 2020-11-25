import numpy as np
from multiprocessing import Pool, TimeoutError
import os,time

def f(x):
    #xx=np.random.randn(2048,2048)
    #for i in range(10):
    #    y=xx@xx
    return x*x

if __name__ == '__main__':
    n=4096
    x=np.random.rand(n,n)
    y=np.empty([n,n//2+1],dtype='complex')
    t1=time.time()
    with Pool(processes=4) as pool:
        #print(pool.map(f,range(10)))
        #for i in pool.imap_unordered(f, range(10)):
        #    print(i)        
        for i in range(n):
            res=pool.apply_async(np.fft.rfft,(x[i,:],))
            y[i,:]=res.get()
        #res = pool.apply_async(os.getpid, ())
        #print(res.get(timeout=1))
    t2=time.time()
    print('pool took ',t2-t1,' to do fft')
    print(np.sum(x))
    print(np.sum(y[:,0]))
    t1=time.time()
    yy=np.fft.rfft(x,axis=1)
    t2=time.time()
    print('direct took ',t2-t1,' to do fft')
    print('standard deviation from pool vs. regular is ',np.std(yy-y))
