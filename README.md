# Slow Control DUNE DB
Extract and Store ProtoDUNE Slow Control database

To get the data from json to csv:

curl http://.../day/YY-MM-DD/ID > output.json

By using a simple python script, we can transform the json file to a .csv file:

import json, csv

with open('output.json', 'r') as f:

    d = json.load(f)

with open('output.csv','w') as f:

    w = csv.writer(f)
    w.writerows(d.items())

