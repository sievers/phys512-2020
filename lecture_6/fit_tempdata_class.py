import numpy as np
import xlrd
from matplotlib import pyplot as plt
import ratfit

crud=xlrd.open_workbook('A02_GAIN_MIN20_373.xlsx')
sheet=crud.sheet_by_index(0)

nu=np.asarray(sheet.col_values(0))
nu=nu/1e6 #convert frequency from Hz to MHz
gain=np.asarray(sheet.col_values(1))

nu_min=15

ii=nu>nu_min
nu=nu[ii]
gain=gain[ii]

#rescale frequency to go from -1 to 1
nu_scale=nu-nu.min()
nu_scale=nu_scale/nu_scale.max()
nu_scale=2*nu_scale-1
order=4
#get the A matrix
A=np.polynomial.legendre.legvander(nu_scale,order)
#do the least-squares fit
fitp=np.linalg.inv(A.T@A)@(A.T@gain)
#evaluate the fit at the point we're after
pred=A@fitp

#what is the noise on the data points?
rms=np.std(gain-pred)
N=rms**2
chisq=np.sum((gain-pred)**2)/N**2
print("RMS scatter about fit is ",rms)

Ninv=np.eye(len(gain))/N
lhs=A.T@Ninv@A
errs=np.sqrt(np.diag(np.linalg.inv(lhs)))
for i in range(len(fitp)):
    print('paramter ',i,' has value ',fitp[i],' and error ',errs[i])

pred_cov=A@(np.linalg.inv(lhs)@A.T)


assert(1==0)


pp=np.polyfit(nu,gain,5)
pred_poly=np.polyval(pp,nu)
print('RMS error after fit is ' + repr(np.sqrt(np.mean( (pred_poly-gain)**2))))

plt.ion()
plt.clf()
#plt.plot(nu,gain)
plt.plot(nu,gain-pred_poly)


n=3
m=2
xx=np.linspace(nu[0],nu[-1],n+m)
yy=np.polyval(pp,xx)
aa,bb=ratfit.ratfit_exact(xx,yy,n,m)
aa2,bb2=ratfit.ratfit_lsqr(nu,gain,aa,bb)
pred_rat=ratfit.rateval(aa2,bb2,nu)
print('RMS error after rational function fit is ' + repr(np.sqrt(np.mean( (pred_rat-gain)**2))))
plt.plot(nu,gain-pred_rat)



