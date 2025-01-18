a=int(input("Enter the number: "))


*Method 1 (Iteration):
if a<0:
    print("The number is negative hence factorial cannot be calculated!")
elif a<2:
    print(f'Factorial is: 1')
else:       
    for i in range(2,a):
        a=a*i
    print(f'Factorial is: {a}')


*Method 2 (Recursion):
def factorial(x):
    if a<0:
        return "The number is negative hence factorial cannot be calculated!"
    elif a<2:
        return 1
    else:
        return x*factorial(x-1)
fact=factorial(a)
print(f"The factorial of {a} is {fact}")
