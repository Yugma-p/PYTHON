#Write a Python program to #read specific columns of a given  csvfile and print the content of the columns.
import os
os.chdir("/home/mca/Desktop/yugma/python/c05")
import csv
with open('h.csv',newline='')as csvfile1:
    data=csv.DictReader(csvfile1)
    print("name")
    print("----")
    for i in data:
        print(i['name'])
