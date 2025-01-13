def octal_to_decimal(octal_str):
    decimal = 0
    power = 0
    
    for digit in reversed(octal_str):
        decimal += int(digit) * (8 ** power)
        power += 1
    
    return decimal

octal_str = input("Enter the number in Octal: ")
decimal_value = octal_to_decimal(octal_str)
print(f"The decimal value of octal {octal_str} is {decimal_value}")