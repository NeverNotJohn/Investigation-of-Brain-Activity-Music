import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

df = (pd.read_csv("test_data\BrainFlow-RAW_2023-02-10_23-48-13_7.csv", sep="\t"))

ch_2 = df.iloc[:, 3]

print(ch_2)

plt.specgram(ch_2.values, NFFT=256, Fs=200, cmap="rainbow")
plt.colorbar()
plt.ylabel("Freq (hz)")
plt.xlabel("Time (s)")
plt.show()