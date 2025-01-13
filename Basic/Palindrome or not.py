#Reversing the digits of a number
a=input("Number: ")
d=a[::-1]

if d==a:
    print("The number is palindrome!")
else:
    print("The number is not palindrome!")