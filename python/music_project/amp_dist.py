import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sc
from scipy import signal

""" Take input """

fileName_alpha = "RB-Alpha-T1_music_one.csv"
fileName_stim = "RB-Stim-T1_music_one.csv"

df = pd.read_csv(f"alpha_music\sep_data\music_one\{fileName_alpha}", sep=",")
df_no = pd.read_csv(f"stim_music\sep_data\music_one\{fileName_stim}", sep=",")

sample_rate = 200

lower_bounds = 0 * sample_rate                                                   # seconds input * sample_rate hz sample rate
upper_bounds =  25 * sample_rate

ch_2_music = df.loc[lower_bounds:upper_bounds, " EXG Channel 1"]
ch_2_no_music = df_no.loc[lower_bounds:upper_bounds, " EXG Channel 1"]

dt = (ch_2_music.index.tolist())               # dt = change in time... x-axis of plot
dt_no = (ch_2_no_music.index.tolist())

for i in range(len(dt)):                        # dt[index] = index / frequency of data collection
    dt[i] = i / sample_rate                     # ganglion records 200 data points a second (200 hz)


""" FILTERING DATA """

ch_2_music = ch_2_music.to_numpy()

sos = signal.butter(4, [8, 13], btype='bandpass', output='sos', fs=sample_rate)

ch_2_alpha_music = signal.sosfilt(sos, ch_2_music)
ch_2_stim_music = signal.sosfilt(sos, ch_2_no_music)

peaks_music, _ = signal.find_peaks(ch_2_alpha_music, prominence=0.3)
peaks_stim, _ = signal.find_peaks(ch_2_stim_music, prominence=0.3)

dt = np.array(dt)
dt_no = np.array(dt_no)


"""

# Plot Peaks

plt.plot(dt, ch_2_alpha_music)
plt.plot(dt[peaks_music], ch_2_alpha_music[peaks_music], "x")
plt.xlabel("Time (s)")
plt.ylabel("Volts (µV)")
plt.title("Music Signal with Peaks")
plt.show()

"""

""" GET LIST OF PEAK AMPLITUDES """

peaks_music_list = ch_2_alpha_music[peaks_music]
peaks_no_music_list = ch_2_stim_music[peaks_stim]

""" GENERATE HISTOGRAM """

fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1, constrained_layout=True)
fig.suptitle(f"Amplitude Distribution Alpha music vs Stim music - ALPHA BRAIN WAVES")

ax1.set_title(f"Alpha Music - {fileName_alpha}")
ax1.hist(peaks_music_list, bins=50)
ax1.set_xlabel('Amplitude (µV)')
ax1.set_ylabel('Frequency (# of peaks)')
ax1.set_title('Alpha Music')

ax2.set_title(f"Stim Music - {fileName_stim}")
ax2.hist(peaks_no_music_list, bins=50)
ax2.set_xlabel('Amplitude (µV)')
ax2.set_ylabel('Frequency (# of peaks)')
ax2.set_title('Stim Music')

plt.show()