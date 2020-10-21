import numpy as np
from matplotlib import pyplot as plt

x=np.random.randn(1000)
xft=np.fft.rfft(x)
plt.ion()
plt.clf()
plt.plot(np.abs(xft)**2)

