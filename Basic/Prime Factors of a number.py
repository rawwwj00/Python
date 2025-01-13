def primefactors(a):
    x=[]
    prime=[]
    for i in range(2,a+1):
        if a%i==0:
            x.append(i)
    for j in range(2,max(x)+1):
        b=True
        for k in range(2,j):
            if j%k==0:
                b=False
        if b==True:
            prime.append(j)
    c=set(x)
    d=set(prime)
    print(f"\nAll prime factors of {a} are:\n")
    return list(c.intersection(d))

b=int(input("Enter a number:"))
print(primefactors(b))