import numpy as np

def get_entropy(freqs):
    freqs=freqs[freqs>0]
    s=-np.sum(freqs*np.log2(freqs))
    return s

f=open('letter_frequency.txt')
ll=f.readlines()
f.close()

tmp=ll[1].split()
nlang=len(tmp)-1
nlet=len(ll)-1
freq=np.zeros([nlet,nlang])
for i in range(nlet):
    tags=ll[i+1].split()
    for j in range(nlang):
        tt=tags[j+1]
        tt=tt.replace('%','')
        tt=tt.replace('*','')
        tt=tt.replace('~','')
        tt=tt.replace('(','')
        tt=tt.replace(')','')
        freq[i,j]=np.double(tt)/100

langs=ll[0].split()
langs=langs[1:]
for i in range(nlang):
    print('language ',langs[i].strip(),' has entropy ',get_entropy(freq[:,i]))


hawaiian=np.asarray([2089,849,844,671,660,576,541,472,357,354,259,239,74])
hawaiian=hawaiian/hawaiian.sum()
print('and Hawaiian has an entropy of ',get_entropy(hawaiian))
