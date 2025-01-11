def Armstrong(a,b):
    print(f"\nArmstrong Number between the {a} and {b} are: ")
    for i in range(a,b+1):
        a=list(str(i))
        b=0
        for j in range(len(a)):
            b+=(int(a[j])**len(a))
            if b==i:
                print(i)

print("\nArmstrong Number between entered range:\n")
x=int(input("From:"))
y=int(input("To:"))
Armstrong(x,y)