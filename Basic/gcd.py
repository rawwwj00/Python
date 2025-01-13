def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))
print(gcd(x,y))