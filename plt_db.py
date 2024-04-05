#NilayB #Apr5/2024
#initial code to make the histograms for DBs
#needs conversion the unix time to date time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import sys
import matplotlib.style as style

cols = ["fTimeStamp", "fHighVoltage"]
df = pd.read_csv("data/NP04_DCS_01_Heinz_V_April3.csv", names =cols)
df.head()

print(df)

#sample_data={'fTimeStamp','fHighVoltage'}
#sns.scatterplot(x="fTimeStamp", y="fHighVoltage", data=df)

style.use('dark_background')

df.plot(kind='scatter', x='fTimeStamp', y='fHighVoltage', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(True)
plt.savefig('HV_TimeStamp.png')
plt.show()

sys.exit()
