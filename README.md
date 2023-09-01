# bootstrap_resample_with_replacement
Tekano Mbonani

## System Docs 📃
A combination of codes developed for the calculation of the cross-correlation confidence intervals for a pair of light-curves. The project consists of three codes, the ***bootstrap_LC.py*** for creating artificial light-curves by randomly resampling a pair of light-curves with replacement, ***zdcf95_v2.2.f90*** for executing cross-correlation analysis of the pairs of artificial light-curves, ***helloScriptpt.sh*** is used to execute the previous code, and last is ***significance.py***, which reads the artificial cross-correlations to determine 1-sigma, 2-sigma and 3-sigma confidence intervals.
 

## Software Requirements 🔌
You will need to install the following software on your system in order to run/edit the Python script.
* Mac OS/ Ubuntu 18.04 OS
* Fotran90
* Python 3.10.12
* Textedit/ IDE - spyder or jupyter-notebook
* Python libraries
  * numpy
  * matplotlib
  * astropy
  * scipy
  * glob
  * datetime
