import csv
import re
lst = []
pattern = r'.+/.+/2015'
with open('Crimes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if re.match(pattern, row[2]):
            lst.append(row[5])
    print(max(lst, key=lst.count))

