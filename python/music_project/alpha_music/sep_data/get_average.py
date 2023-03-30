import pandas as pd
import os

# READ AVERAGE VALUE GRAPH


"""   Read File   """

# CHANGE THIS VAR TO GET NEXT FOLDER
directory = 'music_one'

dataFrameList = []

for filename in os.listdir(directory):
    
    f = os.path.join(directory, filename)
    # checking if it is a file
    
    if os.path.isfile(f):
        
        """   Read Files and add to list  """

        df = pd.read_csv(f, sep=",")
        dataFrameList.append(df)
 
print(dataFrameList[0])  

avgDataFrame = dataFrameList[0]

for i in range(1, len(dataFrameList)):
    avgDataFrame = avgDataFrame.add(dataFrameList[i])

avgDataFrame = avgDataFrame / len(dataFrameList)
  
    
print(avgDataFrame)

avgDataFrame.to_csv(f"music_one\\average\\average_waveform.csv") 

"""
    NOTES:
    
    - Big ass values cancel out the other values... 

"""