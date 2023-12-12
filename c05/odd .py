#Python program to copy odd lines of one file to other
f1=open('black.txt','r')
f2=open('file.txt','w')
content=f1.readlines()
print("Content", content)
for i in range(0,len(content)):
    if(i%2==0):
           f2.write(content[i])
    else:
           pass
f2.close()
f2=open('file.txt','r') 
content1=f2.read() 
print("\nodd lines\n\n",content1) 
f2.close()
