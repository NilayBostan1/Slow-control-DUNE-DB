#NilayBostan #April18/2024
import requests
import json, csv
import os, sys, time, subprocess
import argparse
#from ucondb.webapi import UConDBClient
import shutil, re
import matplotlib.pyplot as plt
import pandas as pd
from subprocess import run

response = requests.get('http://[CERN URL]/day/2023-09-07/46262626262')
sys.stdout = open('output.json','wt')
print(response.text)

with open('output.json', 'r') as f:
    d = json.load(f)

with open('output.csv','w') as f:
    w = csv.writer(f)
    w.writerows(d.items())
    
run_number = '1010'
ucon_folder = 'test'
ucon_object = 'test'
#run_number = str(run_number)
username = 'test'
password = 'test'
   
     
#run_dir = str(run_number)
#blob_str = 'blob_' + run_number + '.txt'
 
ucondb_url = 'https://dbdata0vm.fnal.gov:9443/protodune_ucon_prod/app/data/' + ucon_folder + '/' + ucon_object + '/key=' + run_number
ret_code = subprocess.run(['curl','-T', 'output.csv','--digest','-u','username:password','-X','PUT', ucondb_url])

    
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
