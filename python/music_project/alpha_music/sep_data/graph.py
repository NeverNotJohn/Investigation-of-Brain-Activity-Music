import matplotlib.pyplot as plt
import pandas as pd
import scipy as sc
from scipy import signal

"""   Read File and separate to different channels   """

name = "RG Alpha T2: Music Section 1"

df = pd.read_csv("music_one\OpenBCI-RAW-2023-03-08_17-13-31-RG-Alpha-T2_music_one.csv", sep=",")

print(df)

sample_rate = 200

ch_2 = df.loc[:, " EXG Channel 1"]
ch_4 = df.loc[:, " EXG Channel 3"]

""" Remove Outliers """

lower = ch_2.quantile(.25)                     # CONTAIN DATA ONLY IN INNER QUARTILE          
upper = ch_2.quantile(.75)
ch_2 = ch_2.clip(lower=lower, upper=upper)

lower = ch_4.quantile(.25)                    
upper = ch_4.quantile(.75)
ch_4 = ch_4.clip(lower=lower, upper=upper)


dt = (ch_2.index.values.tolist())               # dt = change in time... x-axis of plot

print(ch_2)

"""   Create Spectogram   """

plt.title(name)
plt.specgram(ch_2, NFFT=256, Fs=sample_rate, cmap="rainbow")    # chage NFFT???
bar = plt.colorbar()
bar.ax.set_title('Amplitude? ')
plt.ylabel("Freq (hz)")
plt.xlabel("Time (s)")
plt.show()


""" FILTERING DATA """

ch_2 = ch_2.to_numpy()

sos = signal.butter(4, [50, 60], btype='bandpass', output='sos', fs=sample_rate)

ch_2 = signal.sosfilt(sos, ch_2)
ch_4 = signal.sosfilt(sos, ch_4)



"""   Create Time Series Plot   """

for i in range(len(dt)):                        # dt[index] = index / frequency of data collection
    dt[i] = i / sample_rate                     # ganglion records 200 data points a second (200 hz)

fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)

ax1.set_title("Channel 2")
ax2.set_title("Channel 4")

ax1.plot(dt, ch_2)  
ax2.plot(dt, ch_4)              
ax1.set_ylabel("Volts (µV)")
ax1.set_xlabel("Time (s)")              
ax2.set_ylabel("Volts (µV)")
ax2.set_xlabel("Time (s)")              
plt.show()


