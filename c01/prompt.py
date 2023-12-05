#prompot

n=int(input("total number of integers:"))
list1=[]
for i in range(n):
    a=int(input("enter an interger:"))
    if a<100:
        list1.append(a)
    else:
        list1.append("over")
print(list1)


#count the occurance of "a" with in list


name=["kichu","sanam","minnu","saira"]
for i in name:
    print("'a' occurs in",i,"-",i.count('a'),"tims")
            
