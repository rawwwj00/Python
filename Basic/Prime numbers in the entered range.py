def prime_range(a,b):
    lst_prime=[]
    for i in range(a,b):
        c=True
        for j in range(2,i):
            if i%j==0:
                c=False
        if c==True:
            lst_prime+=[i]
    set_prime=set(lst_prime)
    f_list=list(set_prime)
    f_list.sort()
    if 1 in f_list:
        f_list.remove(1)
    for k in range(len(f_list)):
        print(f_list[k])

x=int(input("From: "))
y=int(input("To: "))
prime_range(x,y)
