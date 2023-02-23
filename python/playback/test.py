import matplotlib.pyplot as plt
import pandas as pd

"""   Read File and separate to different channels   """

df = pd.read_csv("test_data\OpenBCI-RAW-2023-02-22_18-06-36.csv", sep=", ", skiprows=4, engine="python")

print(df)

ch_1 = df["EXG Channel 0"]
ch_2 = df["EXG Channel 1"]
ch_3 = df["EXG Channel 2"]
ch_4 = df["EXG Channel 3"]



"""   Print Channel Debug   """

print(ch_2)

"""   Create Spectogram   """

plt.specgram(ch_2.values, NFFT=512, Fs=200, cmap="rainbow")
plt.colorbar()
plt.ylabel("Freq (hz)")
plt.xlabel("Time (s)")
plt.show()

"""   Create Time Series Plot   """

dt = (df.index.values.tolist())         # dt = change in time... x-axis of plot
for i in dt:                            # dt[index] = index / frequency of data collection
    dt[i] = i / 200                     # ganglion records 200 data points a second (200 hz)

plt.plot(dt, ch_2)                
plt.ylabel("Freq (hz)")
plt.xlabel("Time (s)")              
plt.show()

