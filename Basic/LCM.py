def lcm(a,b):
    if a>b:
        a,b=b,a
    c=1
    if b%a==0:
        return b
    else:
        for i in range(1,b+1):
            if a%i==0 and b%i==0:
                c=c*i
        if c==1:
            c=a*b
    return c
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
print(f"The Least Common Multiple (LCM) of {x} and {y} is {lcm(x,y)}.")

print("\n24BCE10022 \n RAJ SACHAN")