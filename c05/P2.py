#import os
import csv
#os.chdir("/home/mca/Desktop/yugma/python/c05")
with open("list.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
