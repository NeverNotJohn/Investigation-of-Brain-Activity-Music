import matplotlib.pyplot as plt
import pandas as pd
import scipy as sc
from scipy import signal
import os

# READ AVERAGE VALUE GRAPH

""" Graph Settings n stuff """
fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)        # figure initialization

ax1.set_title("Channel 2")
ax2.set_title("Channel 4")
ax1.set_ylabel("Volts (µV)")
ax1.set_xlabel("Time (s)")              
ax2.set_ylabel("Volts (µV)")
ax2.set_xlabel("Time (s)")     


"""   Read File   """

# CHANGE THIS VAR TO GET NEXT FOLDER
directory = 'sep_data\music_one'

for filename in os.listdir(directory):
    
    f = os.path.join(directory, filename)
    # checking if it is a file
    
    if os.path.isfile(f):
        print(f)
        
        """   Read File and separate to different channels   """

        df = pd.read_csv(f, sep=",")

        print(df)

        sample_rate = 200

        ch_2 = df.loc[:, " EXG Channel 1"]
        ch_4 = df.loc[:, " EXG Channel 3"]

        """ Remove Outliers """

        """
        lower = ch_2.quantile(.25)                     # CONTAIN DATA ONLY IN INNER QUARTILE          
        upper = ch_2.quantile(.75)
        ch_2 = ch_2.clip(lower=lower, upper=upper)

        lower = ch_4.quantile(.25)                    
        upper = ch_4.quantile(.75)
        ch_4 = ch_4.clip(lower=lower, upper=upper)
        """

        dt = (ch_2.index.values.tolist())               # dt = change in time... x-axis of plot

        print(ch_2)

        """ FILTERING DATA """

        ch_2 = ch_2.to_numpy()

        sos = signal.butter(4, [50, 60], btype='bandpass', output='sos', fs=sample_rate)

        ch_2 = signal.sosfilt(sos, ch_2)
        ch_4 = signal.sosfilt(sos, ch_4)


        """   Create Time Series Plot   """

        for i in range(len(dt)):                        # dt[index] = index / frequency of data collection
            dt[i] = i / sample_rate                     # ganglion records 200 data points a second (200 hz)

        ax1.plot(dt, ch_2)  
        ax2.plot(dt, ch_4)                        
        
plt.show()

"""
    NOTES:
    
    - Big ass values cancel out the other values... 

"""