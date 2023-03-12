import matplotlib.pyplot as plt
import pandas as pd

"""   Read File and separate to different channels   """

df = pd.read_csv("test_data/OpenBCI-RAW-2023-03-07_18-30-02-DS-Alpha-T4.csv", sep=",", skiprows=4)

print(df)

lower_bounds = (int(input("Input lower bounds in seconds: "))) * 200     # seconds input * 200 hz sample rate
upper_bounds = (int(input("Input upper bounds: "))) * 200  


ch_2 = df.loc[lower_bounds:upper_bounds, " EXG Channel 1"]
ch_4 = df.loc[lower_bounds:upper_bounds, " EXG Channel 3"]


"""   Print Channel Debug   """

print(ch_2)

"""   Create Spectogram   """

plt.specgram(ch_2.values, NFFT=10000, Fs=200, cmap="rainbow")    # chage NFFT???
plt.colorbar()
plt.ylabel("Freq (hz)")
plt.xlabel("Time (s)")
plt.show()

"""   Create Time Series Plot   """

dt = (ch_2.index.values.tolist())         # dt = change in time... x-axis of plot

for i in range(len(dt)):                            # dt[index] = index / frequency of data collection
    dt[i] = i / 200                     # ganglion records 200 data points a second (200 hz)

plt.plot(dt, ch_2)                
plt.ylabel("Volts (mV)")
plt.xlabel("Time (s)")              
plt.show()

