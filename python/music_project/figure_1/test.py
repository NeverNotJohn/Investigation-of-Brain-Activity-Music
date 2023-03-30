import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# generate a signal with peaks
x = np.linspace(0, 6*np.pi, 1000)
signal = np.sin(x) + 0.2*np.sin(3*x) + 0.3*np.sin(5*x)

# detect the peaks
peaks, _ = find_peaks(signal, prominence=0.3)

print(peaks)

# plot the signal and peaks
plt.plot(x, signal)
plt.plot(x[peaks], signal[peaks], "x")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Signal with Peaks")
plt.show()