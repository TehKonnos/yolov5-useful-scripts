import os
import csv
from csv import DictReader


file1 = 'zeroClasses.txt'
file2 = 'classes2.csv'


dict1 = {}
reader1 = open(file1)
for line in reader1:
    key, value = line.split("\n")
    dict1[key] = key


dict2 = {}
lines = list()
#reader2 = csv.DictReader(open(file2))
with open(file2, 'r') as readFile:
    reader = csv.reader(readFile, delimiter=',')
    next(reader)
    for ticket, asset in reader:
        #dict2.setdefault(ticket, []).append(asset)
        dict2[ticket]=asset
        

    #for row in reader:
        #print(row)
    for key in dict2.keys():
        if key not in dict1.keys():
           # lines.append(row)
           lines.append(key)

counter=0
with open('new-classes2.csv', 'w+') as writeFile:
    writer = csv.writer(writeFile, delimiter=',',lineterminator='\n')
    for new_row in lines:
        #writer.writerows(new_row)
        writer.writerow([counter,dict2[new_row]])
        counter = counter+1


#print(set(dict1.keys()).intersection(dict2.keys()))