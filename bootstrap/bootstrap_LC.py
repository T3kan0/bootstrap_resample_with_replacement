import os
import sys

import numpy as np
import os
from astropy.io import fits
from astropy.table import Table
import astropy.units as u
from astropy.time import Time
from astropy.io import votable
import glob
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from matplotlib import style
from matplotlib import rc
import matplotlib.ticker as ticker
from scipy.optimize import curve_fit
from datetime import datetime


start_time = datetime.now()

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1,
                                         sharex=True,
                                         gridspec_kw = {'height_ratios':[8.5,
                                                                         8.5,
8.5,
8.5], 'hspace': 0.4})

print('Uploading Optical & gamma-ray data files.....')
optRdat = np.genfromtxt('3C279_R_flr.txt', 
                      names = True, 
                      autostrip=True, 
                      delimiter = ' ')
optVdat = np.genfromtxt('3C279_V_flr.txt', 
                      names = True, 
                      autostrip=True, 
                      delimiter = ' ')
gamma = np.genfromtxt('3C279_2014_2019_F1_12hr_LC.asc', 
                      names = True, 
                      autostrip=True, 
                      delimiter = '')
print('Sorting the gamma-ray data...')
gammadat = np.sort(gamma, order='MID_MJD')
gamask = (gamma['MID_MJD'] >= 57185.00) & (gamma['MID_MJD'] <= 57194.50)

gammadat = gamma[gamask]
ax1.errorbar(gammadat['MID_MJD']-57100.00,
                 y=gammadat['Flux'],
                 yerr=gammadat['FluxErr'],
                 fmt='o', 
                 #uplims=uplim,
                 c='black',
                 ms=3.0,
                 label = '6hours')
ax1.ticklabel_format(style='sci', axis = 'y', scilimits = (-3,3),
                         useMathText=True)

legends = ax1.legend(loc='upper right', shadow=True, fontsize='large')
legends.get_frame().set_facecolor('red')
plt.draw()
ax1.legend(fontsize=6)
ax1.yaxis.offsetText.set_visible(True)
ax1.set_ylabel('F$_{\\gamma}$', fontsize= 8.0)
ax1.axvline(x=89.12,linewidth=0.2, linestyle='--',color='k' )


ax2.errorbar(optRdat['MJD']-57100.00,
                 y=optRdat['Flux_R'],
                 yerr=optRdat['Flux_R_err'],
                 fmt='o', 
                 # uplims=uplim,
                 c='red',
                 ms=2.0,
                 label = 'R')
ax2.errorbar(optVdat['MJD']-57100.00,
                 y=optVdat['Flux_V'],
                 yerr=optVdat['Flux_V_err'],
                 fmt='o', 
                 # uplims=uplim,
                 c='green',
                 ms=2.0,
                 label = 'V')
ax2.ticklabel_format(style='sci', axis = 'y', scilimits = (-3,3),
                         useMathText=True)
legends = ax2.legend(loc='upper left', shadow=False, fontsize='small')
legends.get_frame().set_facecolor('white')
plt.draw()
ax2.yaxis.offsetText.set_visible(True)
ax2.set_ylabel('F$_{opt}$', fontsize= 8.0)
ax2.axvline(x=89.2393508334,linewidth=0.2, linestyle='--',color='red' )
ax2.axvline(x=89.200528,linewidth=0.2, linestyle='--',color='green')
ax2.axvline(x=88.96903,linewidth=0.2, linestyle='--',color='blue' )

####################################################################
#########  gamma_LC Bootsrap, fake "light-curves"

Tg, Fg, EFg = gammadat['MID_MJD'], gammadat['Flux'], gammadat['FluxErr']
Tr, Fr, EFr = optRdat['MJD'], optRdat['Flux_R'], optRdat['Flux_R_err']
Tv, Fv, EFv = optVdat['MJD'], optVdat['Flux_V'], optVdat['Flux_V_err']

print('Running the bootsrap with replacement analysis..')
for i in range(10):  #so B=3
    sg = np.random.randint(0, len(Fg), len(EFg))
    
    Tg_r = Tg.copy()
    Fg_r = Fg[sg]
    EFg_r = EFg[sg]

    gdat = np.vstack([Tg_r, Fg_r, EFg_r])
    gdat = gdat.T
    
    LC_direct = '/Users/tekanombonani/Desktop/bootstrap/LC' + str(i) + '/'
    os.makedirs(LC_direct, exist_ok=False)
    np.savetxt('/Users/tekanombonani/Desktop/bootstrap/LC' + str(i) + '/' + 'G0.txt', gdat)

    sr = np.random.randint(0, len(Fr), len(EFr))

    Tr_r = Tr.copy()
    Fr_r = Fr[sr]
    EFr_r = EFr[sr]

    rdat = np.vstack([Tr_r, Fr_r, EFr_r])
    rdat = rdat.T

    np.savetxt('/Users/tekanombonani/Desktop/bootstrap/LC' + str(i) + '/' + 'R0.txt', rdat)

    sv = np.random.randint(0, len(Fv), len(EFv))

    Tv_r = Tv.copy()
    Fv_r = Fv[sv]
    EFv_r = EFv[sv]

    vdat = np.vstack([Tv_r, Fv_r, EFv_r])
    vdat = vdat.T

    np.savetxt('/Users/tekanombonani/Desktop/bootstrap/LC' + str(i) + '/' + 'V0.txt', vdat)

    

    R_files = glob.glob('LC_direct/''R0.txt')
    V_files = glob.glob('LC_direct/''V0.txt')
    G_files = glob.glob('LC_direct/''G0.txt')

    for file in R_files:

        a, b, c = np.loadtxt(file,unpack=True)

    for file in V_files:

        A, B, C = np.loadtxt(file,unpack=True)

    for file in G_files:

        aa, bb, cc = np.loadtxt(file,unpack=True)
    
    
        ax4.errorbar(a-57100, b , c)
        ax4.errorbar(A-57100, B , C)
        ax4.set_ylabel('Fs$_{opt}$', fontsize= 8.0)
        ax3.errorbar(aa-57100, bb , cc)
        ax3.set_ylabel('Fs$_{\\gamma}$', fontsize= 8.0)
        ax4.set_xlabel('Time (MJD-57100.00)', fontsize= 9.0)
        ax3.ticklabel_format(style='sci', axis = 'y', scilimits = (-3,3),
                         useMathText=True)
        ax4.ticklabel_format(style='sci', axis = 'y', scilimits = (-3,3),
                         useMathText=True)



#plt.show()
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))










