#Counting vowels from the string
z=input("Enter the text: ")
x=z.lower()
y=len(x)
a=0
e=0
i=0
o=0
u=0
for k in range(0,y):
    c=x[k]
    if c=='a':
        a+=1
    elif c=='e':
        e+=1
    elif c=='i':
        i+=1
    elif c=='o':
        o+=1
    elif c=='u':
        u+=1
tt=a+e+i+o+u
print("Total vowels: ",tt,'\n','a=',a,'\n','e=',e,'\n','i=',i,'\n','o=',o,'\n','u=',u)