import pandas as pd

"""   Read File and separate to different channels   """

file_name = "OpenBCI-RAW-2023-03-07_18-30-02-DS-Alpha-T4.csv"                    # change file name here
path = f"raw_data\{file_name}"


df = pd.read_csv(path, sep=",", skiprows=4)

print(df)

sample_rate = 200

lower_bounds = (int(input("Input lower bounds in seconds: "))) * sample_rate     # seconds input * sample_rate hz sample rate
upper_bounds = (int(input("Input upper bounds: "))) * sample_rate  


ch_2 = df.loc[lower_bounds:upper_bounds, " EXG Channel 1"]
ch_4 = df.loc[lower_bounds:upper_bounds, " EXG Channel 3"]


ch_2 = ch_2.to_frame()

print(ch_2)

ch_2.to_csv('sleep/out.csv')