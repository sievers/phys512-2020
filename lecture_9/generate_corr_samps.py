import numpy as np

n=5
#first, generate a postive definite matrix
x=np.random.randn(n,n)
mat=x.T@x #this is guaranteed to be positive at least semi-definite

nsim=100000
dat_uncorr=np.random.randn(n,nsim)
L=np.linalg.cholesky(mat)
dat_corr=L@dat_uncorr #these data are now correlated, and match the correlations in mat
mat2=(dat_corr@dat_corr.T)
mat2=mat2/nsim
print('original matrix:')
print(mat)
print('covariance of simulated correlated data:')
print(mat2)
print('difference:')
print(mat2-mat)
