x= list(map(int, input().split()))
def avg(x):
    y=len(x)
    c=0
    for i in range(0,y):
        c+=x[i]
    d= float(c/y)
    return d
print(avg(x))