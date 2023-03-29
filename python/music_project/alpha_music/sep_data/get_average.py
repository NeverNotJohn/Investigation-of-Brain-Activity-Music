import pandas as pd
import os

# READ AVERAGE VALUE GRAPH


"""   Read File   """

# CHANGE THIS VAR TO GET NEXT FOLDER
directory = 'music_one'

index = 0

for filename in os.listdir(directory):
    
    f = os.path.join(directory, filename)
    # checking if it is a file
    
    if os.path.isfile(f):
        print(f)
        
        index = index + 1
        
        """   Read File and separate to different channels   """

        df = pd.read_csv(f, sep=",")

        print(df)

        sample_rate = 200

        ch_2 = df.loc[:, " EXG Channel 1"]
        ch_4 = df.loc[:, " EXG Channel 3"]


"""
    NOTES:
    
    - Big ass values cancel out the other values... 

"""