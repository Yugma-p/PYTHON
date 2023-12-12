import csv
csv_col=['id','name','country']
dict_data=[{'id':1,'name':'alex','country':'india'},{'id':2,'name':'aleena','country':'india'},{'id':3,'name':'alexa','country':'india'},{'id':4,'name':'alexan','country':'india'}]
csv_file="Name.csv"
try:
    with open(csv_file,'w')as file1:
        writer=csv.DictWriter(file1,fieldnames=csv_col)
        writer.writeheader()
        for data1 in dict_data:
            writer.writerow(data1)
except IOError:
    print("I/O error")

data1=csv.DictReader(open(csv_file))
print("csv file as adictionary:\n")
for row in data1:
    print(row)
          
