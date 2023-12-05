#split



filename=input("enter the filename:")
extension=filename.split(".")
print("the extension of the file is:",extension[-1])



#compute n+nn+nn

n=int(input("enter an integer:"))
nn=n*11
nnn=n*111
s=n+nn+nnn
print(f"{n}+{nn}+{nnn}={s}")





#swapp

s=input("enter first string:")
s1=input("enter second integer:")
print(s1[0]+s[1:]," ",s[0]+s1[1:])


#sort dic in ascending and desending order


my_dict={"banana":3,"cherry":1,"apple":2,"dates":4}
print("original list:",my_dict)
asorted_dict=dict(sorted(my_dict.items()))
print("ascending order:",asorted_dict)
dsorted_dict=dict(sorted(my_dict.items(),reverse=True))
print("descening order:",dsorted_dict)





#merge 2 dict

dict1={"name":"alice","age":25}
dict2={"name":"ammu","occupation":"se","hobbie":["read","write",]}
dict1.update(dict2)
print(dict1)



#gcd of 2 numbers


num1=int(input("enter an  1 number:"))
num2=int(input("enter an  2 number:"))
if num1<num2:
    min=num1
else:
    min=num2
    gcd=1
for i in range(1,min+1):
    if num1%i==0 & num2%i==0:
        gcd=i
print(f"the gcd of {num1} & {num2} is {gcd}")




#create a list removing even number

list1=[1,2,3,4,5,6,7,8,9,10]
print(f"original list:{list1}")
list2=[x for x in list1 if x%2!=0]
print(f"list of odd number:{list2}")
                 
