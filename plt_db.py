#NilayB #Apr5/2024
#initial code to make the histograms for DBs
#needs conversion the unix time to date time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import sys

cols = ["fTimeStamp", "fHighVoltage"]
df = pd.read_csv("/data/NP04_DCS_01_Heinz_V_Apr3.csv", names =cols)
df.head()

print(df)

#sample_data={'fTimeStamp',
 #     'fHighVoltage'}
#sns.scatterplot(x="fTimeStamp", y="fHighVoltage", data=df)


df.plot(kind='scatter', x='fTimeStamp', y='fHighVoltage', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(True)
plt.savefig('HV_TimeStamp.png')
plt.show()

sys.exit()
