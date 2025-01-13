a=input("Enter your string:")
b={}
for i in range(len(a)):
    c=a[i]
    count=1
    for j in range(i+1,len(a)):
        if a[j]==c:
            count+=1
        else:
            break
    if (c in b) and b[c]<count:
        b[c]=count
    if (c not in b):
        b[c]=count
x=list(b.values())
y=list(b.keys())
position=x.index(max(x))
if position==1:
    print(y[position],f'is repeated {max(x)} times.')
else:
    print("No alphabets were repeated together !!")