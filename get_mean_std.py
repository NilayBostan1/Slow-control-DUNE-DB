#NilayB #May1_2024
#the script to get the mean, std etc of the data from exist CSV file for specific run number
import numpy as np
import json, csv
import pandas as pd

cols = ["fTimeStamp", "fHighVoltage"]
# Read the CSV file
df = pd.read_csv('output.csv', names=cols, header=None)
df.head()
hv_mean = df['fHighVoltage'].mean()
hv_std = df['fHighVoltage'].std()
hv_var = df['fHighVoltage'].var()
hv_sum = df['fHighVoltage'].sum()
# Print the stats
print("High Voltage Mean for the run number 24380: ", hv_mean)
print("High Voltage Std for the run number 24380: ", hv_std)
print("High Voltage Variance for the run number 24380: ", hv_var)
print("High Voltage Sum for the run number 24380: ", hv_sum)
