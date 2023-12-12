import csv
with open("list.csv","r") as file:
    S=csv.reader(file)
    for row in S:
        print(row)
