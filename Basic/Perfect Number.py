x=int(input("Enter the number: "))
c=0
for i in range(1,x):
    if x%i==0:
        c+=i
print("The sum of factors=",c)
if c==x:
    print("The number is a perfect number!")
else:
    print("The number is not a perfect number!")