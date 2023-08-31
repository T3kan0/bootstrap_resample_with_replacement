#!/usr/bin/env python
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
fig, (ax1) = plt.subplots(1, 1,
                                         sharex=False,
                                         gridspec_kw = {'height_ratios':[8.5], 'hspace': 0.3})

files = glob.glob('*/**/*.dcf',
                 recursive=True)



for file in files:
    tau, pt_err, nt_err, zdcf_r, pr_err, nr_err, bins = np.loadtxt(file,unpack=True)
    
    plt.plot(tau, zdcf_r)
    
plt.xlabel('tau')
plt.ylabel('r')
#plt.show()


significance = np.zeros([len(tau), 4])

i=0
for t in tau:

    temp_array = np.array([])

    for file in files:
        tau, pt_err, nt_err, zdcf_r, pr_err, nr_err, bins = np.loadtxt(file,unpack=True)
        temp_array = np.append(temp_array, zdcf_r[tau==t])

    median = np.median(temp_array)
    top = np.percentile(temp_array[temp_array > 0], 95)
    bottom = np.percentile(temp_array[temp_array < 0], 100-95)

    significance[i,:] = [t, median, bottom, top]
    i+=1


_, medians, bot95, top95 = np.hsplit(significance, 4)

plt.plot(tau, medians)
plt.plot(tau, bot95)
plt.plot(tau, top95)
plt.xlabel('time lag')
plt.ylabel('zdcf')
plt.savefig('2sigma_intervals.png')

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))


