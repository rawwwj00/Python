#Pass Automation (Program will check if pass length is between 6-12 characters, 1 capital,small,number and symbol is present or not?)
b=input("Enter the password: ")
def password(a):
    lower=False
    upper=False
    digit=False
    symbol=False
    length=False
    if len(a)>5 and len(a)<13:
        length=True
    for i in a:
        if i.islower():
            lower=True
        elif i.isupper():
            upper=True
        elif i.isdigit():
            digit=True
        elif i=="@" or i=="#" or i=="$":
            symbol=True
    condition=[lower,upper,digit,symbol,length]
    if False in condition:
        return "Invalid Password!"
    else:
        return "Valid Password!"

print(password(b))