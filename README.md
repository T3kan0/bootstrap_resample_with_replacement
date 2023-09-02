# bootstrap_resample_with_replacement
Tekano Mbonani

## System Docs 📃
A combination of codes developed for the calculation of the z-transformed discrete cross-correlation function (ZDCF) confidence intervals for a pair of light-curves. The project consists of three codes, the ***bootstrap_LC.py*** for creating artificial light-curves by randomly resampling a pair of light-curves with replacement, ***zdcf95_v2.2.f90*** for executing cross-correlation analysis of the pairs of artificial light-curves, ***helloScriptpt.sh*** is used to execute the previous code, and last is ***significance.py***, which reads the artificial cross-correlations to determine 1-sigma, 2-sigma and 3-sigma confidence intervals.
 

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

## Executing the code
First the user must ensure that they have the pair of light-curves (LC1 and LC2) to be simulated in the same directory as all codes. Then the user must decide how many simulations (N) they need for the signicance (I used 10 000 simulations in my MSc), then run the ***bootstrap_LC.py*** code, i.e.,
> $ python bootstrap_LC.py

This will create pair of randomly sampled artificial light-curves in N folders. At this stage, initialize the ZDCF file ***zdcf95_v2.2.f90*** as follows,
> $ gfortran -O3 -o zdcf95 zdcf95_v2.2.f90

Now to run the ZDCF file on all N artificial light-curves, we employ the bash code ***helloScriptpt.sh***.
> $ ./helloScriptpt.sh

This creates a ***.dcf*** file for all N pairs of artificial light-curves, which is what ***numpy*** will use to determine the significance. For this the user can run the final code, 
> $ python significance.py

The user can then save the calculated confidence intervals and use them on the ZDCF of the original pair of light-curves. In this repository, I had N=10, an example of the ZDCF of the artificial light-curves is shown below :arrow_heading_down:

![picture alt align = "center"](https://github.com/T3kan0/bootstrap_resample_with_replacement/blob/main/bootstrap/2sigma_intervals.png)

<img align="center" width="100" height="100" src="https://github.com/T3kan0/bootstrap_resample_with_replacement/blob/main/bootstrap/2sigma_intervals.png">

