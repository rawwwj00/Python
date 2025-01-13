import random as rd
cards=["A",2,3,4,5,6,7,8,9,10,"King","Queen","Jack"]
deck=["Spades","Hearts","Diamonds","Clubs"]
c=[]
for i in deck:
    for j in cards:
        c.append(f"{j} of {i}")
rd.shuffle(c)
for k in c:
    print(k)