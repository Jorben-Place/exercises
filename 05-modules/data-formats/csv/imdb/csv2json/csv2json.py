import json
import csv
import sys

# csvFilePath = 'data1.csv'
# jsonFilePath = 'data1.json'

data = {}
with open(sys.argv[1]) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        name = rows['NAME']
        data[name] = rows

with open(sys.argv[2], 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))
    