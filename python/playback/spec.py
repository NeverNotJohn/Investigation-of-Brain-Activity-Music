import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
# Set the time difference to take picture of
# the the generated signal.
Time_difference = 0.0001
 
# Generating an array of values

data = pd.read_csv("test_data/BrainFlow-RAW_2023-02-10_23-48-13_8.csv")



Time_Array = np.linspace(0, 5, math.ceil(5 / Time_difference))
 
# Actual data array which needs to be plot
Data = 20*(np.sin(3 * np.pi * Time_Array))
 
# Matplotlib.pyplot.specgram() function to
# generate spectrogram
plt.specgram(Data, Fs=6, cmap="rainbow")
 
# Set the title of the plot, xlabel and ylabel
# and display using show() function
plt.title('Spectrogram Using matplotlib.pyplot.specgram() Method')
plt.xlabel("DATA")
plt.ylabel("TIME")
plt.show()