def smallest_pos(a):
    a.sort()
    for i in a:
        if i>0:
            b=0
            d=a.index(i)-1
            while True:
                b+=1
                d+=1
                if d<len(a):
                    if a[d]==b:
                        continue
                    else:
                        return (f"{b} is the smallest +ve number missing in the entered array!")
                
                else:
                    return(f"{a[len(a)-1]+1} is the smallest +ve number missing in the entered array!")
c=list(map(int,input("Enter numbers in list separated with spaces: ").split()))
print(smallest_pos(c))