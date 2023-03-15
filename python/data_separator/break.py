import pandas as pd

"""

    Time Sections:

    sleep: 0 - 1 min
    music: 1 - 5 min
    sleep: ...

    Notes:
        Skip first 5 secs
"""

"""   Read File   """

file_name = "OpenBCI-RAW-2023-03-07_18-30-02-DS-Alpha-T4"                        # change file name here
path = f"raw_data\{file_name}.csv"

df = pd.read_csv(path, sep=",", skiprows=4)
sample_rate = 200

""" Time sections """

lower_bounds = 5 * sample_rate                                                   # seconds input * sample_rate hz sample rate
upper_bounds = 60 * sample_rate     

sleep_one = df.iloc[lower_bounds:upper_bounds, [2,4]]                            # separate into single dataframe

sleep_one.to_csv(f"sleep_one\{file_name}_sleep_one.csv")                         # write file


""" WRITE CSV FILES """




