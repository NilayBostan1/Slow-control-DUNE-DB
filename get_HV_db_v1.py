import requests
import json, csv
import os, sys, time, subprocess
import argparse
#from ucondb.webapi import UConDBClient
import shutil, re
import matplotlib.pyplot as plt
import pandas as pd

response = requests.get('http://[CERN URL]]/day/2023-09-07/47363641049371')
sys.stdout = open('output.json','wt')
print(response.text)

with open('output.json', 'r') as f:
    d = json.load(f)

with open('output.csv','w') as f:
    w = csv.writer(f)
    w.writerows(d.items())
    
cols = ["fTimeStamp", "fHighVoltage"]
# Read the CSV file
df = pd.read_csv('output.csv', names=cols, header=None)
df.head()
#print(df)
# Convert Unix timestamps to datetime objects
df['fTimeStamp'] = pd.to_datetime(df['fTimeStamp'], unit='ms')

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['fTimeStamp'], df['fHighVoltage'], marker='o', linestyle='-', color='b')
plt.title('High Voltage vs. Date')
plt.xlabel('Date')
plt.ylabel('fHighVoltage')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Show plot
plt.show()


