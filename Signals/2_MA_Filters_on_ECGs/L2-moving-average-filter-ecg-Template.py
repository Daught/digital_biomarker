# ## Lab Exercise 2a - Moving Average Filters
# =============================================================================
# 2024-08-27 Reto Wildhaber   
# -----------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import lfilter


#%% Cell (1)
# --------------- loading test signal -----------------------
# Choose between real and synthetic test signal by setting one of them to "True".
if True: # Real ECG Signal
    file_name = 'SECG3_FILT_HP51_3CH_20S_FS2400HZ.csv'
    fs = 2400  # sampling rate [Hz] of recorded signal
    K = fs*3  # number of samples to process. Here: fs*<number of seconds>
    x = np.genfromtxt(file_name, usecols=(1), delimiter=r',', skip_header=0, )[:K]
    
if False: # Syntetic Test signal
    file_name = '(Synthetic Rectangle at 2Hz)'
    fs = 1000  # sampling rate [Hz] of recorded signal
    f = 2 # [Hz] Frequency of rectangular singnal
    K = fs*3  # number of samples to process. Here: fs*<number of seconds>
    x = np.arange(K)%(fs//f) < (0.5*fs//f) # generate rectangular test signal
    
k = np.arange(K) # create time index vector
        
# plot signal
fig, axs = plt.subplots(1, 1, sharex='all', figsize=(10, 2))
fig.tight_layout()
axs.plot(k, x, color='gray')

print("Filename:", file_name)
print("Number of loaded samples: ",K)
print("Total signal duration [s]: ", K/fs)
print("Signal shape and samples "+str(x.shape)+" : "+str(x))

#%% Cell (2) - Applying Moving Average Filter of Length L to the input signal x

# ----- dummy code ---- 
L = 30 # Length of Moving Average filter
h = np.array([1,0,0])  # moving averag filter, impulse response
y = x # apply the convolution y = ( h * x )
y_ = y # dummy code
# ---------------------- 


#%% Cell (3) - Plotting filter results
fig, axs = plt.subplots(1, 1, sharex='all', figsize=(10, 3))
fig.tight_layout()
axs.plot(k, x, lw=1.0, color='gray', label="x (raw ECG)")
axs.plot(k, y, lw=1.0, ls='--', color='blue', label="y (MA)")
axs.plot(k, y_, lw=1.0, ls='-', color='blue', label="y (MA, shifted)")
axs.set_title("Moving Average Filter (L="+str(L)+")")

axs.legend()

plt.show()
