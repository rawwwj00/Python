def decimal_to_octal(decimal_num):
    if decimal_num == 0:
        return '0'
    
    octal_str = ''
    while decimal_num > 0:
        octal_str = str(decimal_num % 8) + octal_str
        decimal_num = decimal_num // 8
    
    return octal_str

decimal_num = int(input("Enter the decimal number: "))
octal_str = decimal_to_octal(decimal_num)
print(f"The octal value of decimal {decimal_num} is {octal_str}")