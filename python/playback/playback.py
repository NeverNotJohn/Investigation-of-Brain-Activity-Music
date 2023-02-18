import argparse
import time

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets


def main():
    BoardShim.enable_dev_board_logger()

    parser = argparse.ArgumentParser()
    # use docs to check which parameters are required for specific board, e.g. for Cyton - set serial port


    params = BrainFlowInputParams()
    params.master_board = BoardIds.GANGLION_BOARD
    params.file = "test_data\BrainFlow-RAW_2023-02-10_23-48-13_8.csv"
    board = BoardShim(BoardIds.PLAYBACK_FILE_BOARD, params)
    
    board.prepare_session()
    board.start_stream ()
    time.sleep(10)
    # data = board.get_current_board_data (256) # get latest 256 packages or less, doesnt remove them from internal buffer
    data = board.get_board_data()  # get all data and remove it from internal buffer
    board.stop_stream()
    board.release_session()

    print(data)


if __name__ == "__main__":
    main()