#largest

list1=[8,6,7,4,5]
list2=[5,4,3,2,1]
if len(list1)==len(list2):
    print("a, the list have same length")
else:
    print("a.list have different length")
    

#check same value or not

list1=[8,6,7,4,5]
list2=[5,4,3,2,1]
print(f"b.sum of list1:{sum(list1)} & sum of list2:{sum(list2)}")
if sum(list1)==sum(list2):
    print(" the list sum to same value")
else:
    print("no same value")



#commom value

list1=[8,6,7,4,5]
list2=[5,4,3,2,1]
common_values=set(list1) & set(list2)
if common_values:
   print(f" common values in both lists:{common_values}")
else:
    print("there are no common vales in both list")


#replace with dollar

    
s=input("enter a word:")
c=s[0]
str1=s.replace(s[0],'$')
print(c+str1[1:])


#string where the first and last character are exchanged

str1=input("enter a string")
print(str1[-1]+str1[1:-1]+str1[0])


#area of circle

r=int(input("enter the radius:"))
area=3.14*r**2
print(f"area of circle:{area}")


#read 3 numbers and find the largest number

n1=int(input("enter a first number:"))
n2=int(input("enter a second number:"))
n3=int(input("enter a third number:"))
if n1> n2 & n1>n3:
    print(f"largest number is:{n1}")
elif n2>n1 &  n2>n3:
    print(f"largest number:{n2}")
else:
    print(f"largset number is:{n3}")
        
      
