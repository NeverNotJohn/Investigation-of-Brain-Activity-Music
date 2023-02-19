import matplotlib.pyplot as plt
import pandas as pd

"""   Read File and separate to different channels   """

df = (pd.read_csv("test_data\BrainFlow-RAW_2023-02-10_23-48-13_7.csv", sep="\t"))
ch_1 = df.iloc[:, 2]
ch_2 = df.iloc[:, 3]
ch_3 = df.iloc[:, 4]
ch_4 = df.iloc[:, 5]



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