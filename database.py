import json
import os
import csv

data ={"emp_details":[{'Name': 'Alex', 'dept_id': 6, 'emp_id': 1},
    {'Name': 'Brad', 'dept_id': 4, 'emp_id': 2},
    {'Name': 'Joey', 'dept_id': 5, 'emp_id': 3},
    {'Name': 'Peter', 'dept_id': 3, 'emp_id': 4},
    {'Name': 'Magnus', 'dept_id': 4, 'emp_id': 5}]}
with open("database.json", "w") as csvfile:
        json.dump( data,csvfile)
        fieldnames = ['Name', 'dept_id', 'emp_id'] 
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(y)

with open("database.json","r") as reader:
    var=json.load(reader)

for i in var['emp_details']:
    print(i)

reader.close
