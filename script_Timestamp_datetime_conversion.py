#NilayB #Apr6
#conversion the unix time to date time using csv file.
import csv
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
import datetime

cols = ["fTimeStamp", "fHighVoltage"]
df = pd.read_csv("data/NP04_DCS_01_Heinz_V_April3.csv", names =cols)
df.head()

print(df)

for value in df['fTimeStamp']:
    mytimestamp = int(value)
    mytime = datetime.datetime.fromtimestamp(mytimestamp/1000)
    print(mytimestamp, mytime)


