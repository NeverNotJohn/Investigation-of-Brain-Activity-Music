import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds

""" SIMULATE BOARD """

# prep stuff
BoardShim.enable_dev_board_logger()
params = BrainFlowInputParams()
params.master_board = BoardIds.GANGLION_BOARD
params.file = "test_data\BrainFlow-RAW_2023-02-10_23-48-13_7.csv"
board = BoardShim(BoardIds.PLAYBACK_FILE_BOARD, params)

# simulation stuff
board.prepare_session()
board.start_stream()
BoardShim.log_message(LogLevels.LEVEL_INFO.value, 'start sleeping in the main thread')
time.sleep(300) # FIXME
data = board.get_board_data()
board.stop_stream()
board.release_session()

""" GATHER DATA """

eeg_channels = BoardShim.get_eeg_channels(BoardIds.SYNTHETIC_BOARD.value)   # not used but useful later?
df = pd.DataFrame(np.transpose(data))                                       # data and sorted
print(df)

ch_3 = df.iloc[:, 3]                                                        # data only in channel 3
 
 
# generate spectrogram
plt.specgram(ch_3.values, NFFT=1024, Fs=200, cmap="rainbow")
plt.colorbar()
plt.ylabel("Freq (hz)") # what
plt.xlabel("Time (s)")
plt.show()