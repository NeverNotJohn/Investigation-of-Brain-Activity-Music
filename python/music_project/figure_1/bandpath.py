import matplotlib.pyplot as plt
import pandas as pd
import scipy as sc
from scipy import signal

"""   Read File and separate to different channels   """

name = "RG Alpha T2: Music Section 1"

df = pd.read_csv("data_music\RR-Alpha-T1_music_one.csv", sep=",")
df_no = pd.read_csv("data_sleep\RR-Alpha-T1_sleep_one.csv", sep=",")

sample_rate = 200

ch_2_music = df.loc[:, " EXG Channel 1"]
ch_2_no_music = df_no.loc[:, " EXG Channel 1"]

dt = (ch_2_music.index.values.tolist())               # dt = change in time... x-axis of plot
dt_no = (ch_2_no_music.index.values.tolist())

print(ch_2_music)

""" FILTERING DATA """

ch_2_music = ch_2_music.to_numpy()

sos = signal.butter(4, [8, 13], btype='bandpass', output='sos', fs=sample_rate)

ch_2_alpha_music = signal.sosfilt(sos, ch_2_music)
ch_2_alpha_no_music = signal.sosfilt(sos, ch_2_no_music)


"""   Create Time Series Plot   """


for i in range(len(dt)):                        # dt[index] = index / frequency of data collection
    dt[i] = i / sample_rate                     # ganglion records 200 data points a second (200 hz)

for i in range(len(dt_no)):
    dt_no[i] = i / sample_rate

fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1, constrained_layout=True)
fig.suptitle("Alpha Waves with vs. Without Music")

ax1.set_title("With Music")
ax2.set_title("Without Music")

ax1.plot(dt, ch_2_alpha_music)  
ax2.plot(dt_no, ch_2_alpha_no_music)              
ax1.set_ylabel("Volts (µV)")
ax1.set_xlabel("Time (s)")              
ax2.set_ylabel("Volts (µV)")
ax2.set_xlabel("Time (s)")              
plt.show()


