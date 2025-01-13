x=int(input("Enter the number: "))
y=str(x)
z=len(y)
k=""
for i in range(z-1,-1,-1):
    k=k+y[i]
print(int(k))