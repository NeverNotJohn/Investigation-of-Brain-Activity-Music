import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds
from brainflow.data_filter import DataFilter

# Set the time difference to take picture of
# the the generated signal.
Time_difference = 0.0001
 
# Generating an array of values
BoardShim.enable_dev_board_logger()
params = BrainFlowInputParams()
params.master_board = BoardIds.GANGLION_BOARD
params.file = "test_data\BrainFlow-RAW_2023-02-10_23-48-13_7.csv"
board = BoardShim(BoardIds.PLAYBACK_FILE_BOARD, params)

board.prepare_session()
board.start_stream()
BoardShim.log_message(LogLevels.LEVEL_INFO.value, 'start sleeping in the main thread')
time.sleep(10)
data = board.get_board_data()
board.stop_stream()
board.release_session()

# demo how to convert it to pandas DF and plot data
eeg_channels = BoardShim.get_eeg_channels(BoardIds.SYNTHETIC_BOARD.value)

df = pd.DataFrame(np.transpose(data))
print(data)
print(df)

print('Data From the Board')
test = df.iloc[:, 3]
 
 
# Matplotlib.pyplot.specgram() function to
# generate spectrogram
plt.specgram(test.values, NFFT=5000, Fs=200, cmap="rainbow")
 
# Set the title of the plot, xlabel and ylabel
# and display using show() function
plt.colorbar()
plt.ylabel("Freq (hz)") # what
plt.xlabel("Time (s)")
plt.show()