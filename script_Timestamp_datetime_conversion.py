#NilayB #Apr6
#conversion the unix time to date time and plot using HV data in csv file
import matplotlib.pyplot as plt
import pandas as pd

csv_file_path = 'data/NP04_DCS_01_Heinz_V_April3.csv'

cols = ["fTimeStamp", "fHighVoltage"]
# Read the CSV file
df = pd.read_csv(csv_file_path, names=cols, header=None)
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
