def str_to_exp(exp):
    def solve_exp(x):
        return eval(exp)
    return solve_exp

a=list(map(int, input().split()))
b=input("Enter your expression: ")
c=str_to_exp(b)
d=c(a[0])
if d==a[1]:
    print(True)
else:
    print(False)
