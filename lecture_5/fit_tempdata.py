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



