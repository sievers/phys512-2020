import numpy as np



def myfft(f):
    if len(f)==1:
        return f
    f_even=f[0::2]
    f_odd=f[1::2]
    N=len(f)
    kvec=np.arange(N/2)
    twid=np.exp(-2J*np.pi*kvec/N)
    
    ft_even=myfft(f_even)
    ft_odd=myfft(f_odd)
    return np.hstack([ft_even+twid*ft_odd,ft_even-twid*ft_odd])

x=np.random.randn(256)
ft1=myfft(x)
ft2=np.fft.fft(x)
print(np.mean(np.abs(ft1-ft2)))
