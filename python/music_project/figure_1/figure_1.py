import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal

""" Read File and separate channels """

df = pd.read_csv("data_music\RR-Alpha-T1_music_one.csv", sep=",")

sample_rate = 200

lower_bounds = 0 * sample_rate          # sec * sampling rate                                          # seconds input * sample_rate hz sample rate
upper_bounds =  30 * sample_rate

ch_2 = df.loc[lower_bounds:upper_bounds, " EXG Channel 1"]
ch_4 = df.loc[lower_bounds:upper_bounds, " EXG Channel 3"]

dt = (ch_2.index.tolist())     

for i in range(len(dt)):                        # dt[index] = index / frequency of data collection
    dt[i] = i / sample_rate                     # ganglion records 200 data points a second (200 hz)


""" FILTERING DATA """

ch_2 = ch_2.to_numpy()
ch_4 = ch_4.to_numpy()

sos_gamma = signal.butter(4, [32, 99], btype='bandpass', output='sos', fs=sample_rate)
sos_beta = signal.butter(4, [13, 32], btype='bandpass', output='sos', fs=sample_rate)
sos_alpha = signal.butter(4, [8, 13], btype='bandpass', output='sos', fs=sample_rate)
sos_theta = signal.butter(4, [4, 8], btype='bandpass', output='sos', fs=sample_rate)
sos_delta = signal.butter(4, [0.5, 4], btype='bandpass', output='sos', fs=sample_rate)

ch_2_gamma = signal.sosfilt(sos_gamma, ch_2)
ch_4_gamma = signal.sosfilt(sos_gamma, ch_4)

ch_2_beta = signal.sosfilt(sos_beta, ch_2)
ch_4_beta = signal.sosfilt(sos_beta, ch_4)

ch_2_alpha = signal.sosfilt(sos_alpha, ch_2)
ch_4_alpha = signal.sosfilt(sos_alpha, ch_4)

ch_2_theta = signal.sosfilt(sos_theta, ch_2)
ch_4_theta = signal.sosfilt(sos_theta, ch_4)

ch_2_delta = signal.sosfilt(sos_delta, ch_2)
ch_4_delta = signal.sosfilt(sos_delta, ch_4)

fig, [gamma, beta, alpha, theta, delta] = plt.subplots(nrows=5, ncols=1, constrained_layout=True)

fig.suptitle("Alpha Music Brain Wave Decomposition")

gamma.set_title("Gamma (32 - 99 Hz)")
beta.set_title("Beta (13 - 32 Hz)")
alpha.set_title("Alpha (8 - 13 Hz)")
theta.set_title("Theta (4 - 8 Hz)")
delta.set_title("Delta (0.5 - 4 Hz)")

gamma.plot(dt, ch_2_gamma)
beta.plot(dt, ch_2_beta)
alpha.plot(dt, ch_2_alpha)
theta.plot(dt, ch_2_theta)
delta.plot(dt, ch_2_delta)

gamma.plot(dt, ch_4_alpha)
beta.plot(dt, ch_4_beta)
alpha.plot(dt, ch_4_alpha)
theta.plot(dt, ch_4_theta)
delta.plot(dt, ch_4_delta)

gamma.set_ylabel("Volts (µV)")
gamma.set_xlabel("Time (s)")
beta.set_ylabel("Volts (µV)")
beta.set_xlabel("Time (s)")
alpha.set_ylabel("Volts (µV)")
alpha.set_xlabel("Time (s)")
theta.set_ylabel("Volts (µV)")
theta.set_xlabel("Time (s)")
delta.set_ylabel("Volts (µV)")
delta.set_xlabel("Time (s)")

plt.show()