a=int(input("Enter the number:"))
sum=0
while a>0:
    b=a%10
    sum+=b
    a=a//10
print(sum)