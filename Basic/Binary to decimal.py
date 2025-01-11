# In the following program, you can convert a binary number (even with decimal point) into decimal
def binary_to_decimal(a):
    b=list(a)
    before_dec=[]
    after_dec=[]
    for i in b:
        if i=='.':
            break
        before_dec.append(i)
    for j in range(len(before_dec)+1,len(b)):
        after_dec.append(b[j])
    c=before_dec[::-1]
    d=list(map(int,c))
    decim=0.0
    for k in range(len(d)):
        decim+=(2**k)*d[k]
    e=list(map(int,after_dec))
    after_de=0.0
    for l in range(len(e)):
        after_de+=(2**-(l+1))*e[l]
    final=decim+(after_de)
    return final
a=input("Enter binary number:")
print(binary_to_decimal(a))