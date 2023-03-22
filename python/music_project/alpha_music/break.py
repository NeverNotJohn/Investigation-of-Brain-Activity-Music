import pandas as pd

"""

    Time Sections:

    sleep: 0 - 1 min
    music: 1 - 5 min
    sleep: ...

    Notes:
        Skip first 5 secs
        1 second buffer
"""

"""   Read File   """

file_name = "OpenBCI-RAW-2023-03-08_17-30-16-RG-Alpha-T3"                        # change file name here
path = f"raw_data\{file_name}.csv"

df = pd.read_csv(path, sep=",", skiprows=4)
sample_rate = 200

""" Time section 1 - Sleep """

lower_bounds = 10 * sample_rate                                                   # seconds input * sample_rate hz sample rate
upper_bounds =  30 * sample_rate     

sleep_one = df.iloc[lower_bounds:upper_bounds, [2,4]]                            # separate into single dataframe

sleep_one.to_csv(f"sep_data\sleep_one\{file_name}_sleep_one.csv")                         # write file


""" Time Section 2 - Music """

lower_bounds = 61 * sample_rate                                                   # seconds input * sample_rate hz sample rate
upper_bounds = 300 * sample_rate     

sleep_one = df.iloc[lower_bounds:upper_bounds, [2,4]]                            # separate into single dataframe

sleep_one.to_csv(f"sep_data\music_one\{file_name}_music_one.csv")                         # write file

""" Time Section 3 - Sleep """

lower_bounds = 301 * sample_rate                                                   # seconds input * sample_rate hz sample rate
upper_bounds = 360 * sample_rate     

sleep_one = df.iloc[lower_bounds:upper_bounds, [2,4]]                            # separate into single dataframe

sleep_one.to_csv(f"sep_data\sleep_two\{file_name}_sleep_two.csv")                         # write file

""" Time section 4 - Music """

lower_bounds = 361 * sample_rate                                                   # seconds input * sample_rate hz sample rate
upper_bounds = 660 * sample_rate     

sleep_one = df.iloc[lower_bounds:upper_bounds, [2,4]]                            # separate into single dataframe

sleep_one.to_csv(f"sep_data\music_two\{file_name}_music_two.csv")                         # write file
