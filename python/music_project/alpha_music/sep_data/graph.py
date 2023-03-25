import matplotlib.pyplot as plt
import pandas as pd
import scipy as sc
from scipy import signal

"""   Read File and separate to different channels   """

name = "DS Alpha T4: Music Section 1"

df = pd.read_csv("music_one\OpenBCI-RAW-2023-03-07_18-30-02-DS-Alpha-T4_music_one.csv", sep=",")

print(df)

sample_rate = 200

ch_2 = df.loc[:, " EXG Channel 1"]
ch_4 = df.loc[:, " EXG Channel 3"]

dt = (ch_2.index.values.tolist())               # dt = change in time... x-axis of plot

print(ch_2)

""" FILTERING DATA """

ch_2 = ch_2.to_numpy()

sos = signal.butter(4, [50, 60], btype='bandpass', output='sos', fs=sample_rate)
# sos = signal.butter(10, 15, 'hp', fs=200, output='sos')

ch_2 = signal.sosfilt(sos, ch_2)

"""   Create Spectogram   """

plt.title(name)
plt.specgram(ch_2, NFFT=256, Fs=sample_rate, cmap="rainbow")    # chage NFFT???
plt.colorbar()
plt.ylabel("Freq (hz)")
plt.xlabel("Amplitude")
plt.show()



"""   Create Time Series Plot   """

for i in range(len(dt)):                        # dt[index] = index / frequency of data collection
    dt[i] = i / sample_rate                     # ganglion records 200 data points a second (200 hz)

plt.title(name)
plt.plot(dt, ch_2)                
plt.ylabel("Volts (µV)")
plt.xlabel("Time (s)")              
plt.show()


