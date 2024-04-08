import json, csv

with open('output.json', 'r') as f:
    d = json.load(f)

with open('csv_file_name_here.csv','w') as f:
    w = csv.writer(f)
    w.writerows(d.items())
