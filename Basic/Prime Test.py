a=int(input("Enter a number:"))
b=False
if a==0 or a==1 or a<0:
    print(a,'is not a prime number')
elif a==2:
    print('2 is a prime number.')
for i in range(2,a):
    if a%i!=0:
        b=True
    else:
        print(a,'is not a prime number.')
        break
if b==True:
    print(a,'is a prime number.')