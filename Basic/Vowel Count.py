x=input("Enter the text: ")
z=x.lower()
y=len(z)
a=0
e=0
i=0
o=0
u=0
for k in range(0,y):
    c=z[k]
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
print("The entered text has: ",'\n',a,':a','\n',e,':e','\n',i,':i','\n',o,':o','\n',u,':u')