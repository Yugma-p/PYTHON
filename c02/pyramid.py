#display the pyramid

def disp_pyramid(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i*j,end=" ")
        print( )
n=int(input("enter the number of steps:"))
if n<1:
    print("please enter a positive integer:")
else:
    disp_pyramid(n)




#string using dictionary


def countchar(inputstring):
    count={}
    for char in inputstring:
        if char in count:
            count[char]+=1
        else:
            count[char]=1
    return count
str2=input("enter a string:")
result=countchar(str2)
print(result)



#add ly

def modifystr(str1):
    if str1.endswith("ing"):
        return str1+"ly"
    else:
        return str1+"ing"
str1=input("enter a string")
result=modifystr(str1)
print(result)




#return longest word


# function to find the longest
# length in the list
def longestLength(a):
	max1 = len(a[0])
	temp = a[0]

	# for loop to traverse the list
	for i in a:
		if(len(i) > max1):

			max1 = len(i)
			temp = i

	print("The word with the longest length is:", temp,
		" and length is ", max1)


# Driver Program
a = ["one", "two", "third", "four"]
longestLength(a)



