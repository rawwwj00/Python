def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return '0'
    
    binary_str = ''
    while decimal_num > 0:
        binary_str = str(decimal_num % 2) + binary_str
        decimal_num = decimal_num // 2
    
    return binary_str

decimal_num = int(input("Enter the number in decimal form: "))
binary_str = decimal_to_binary(decimal_num)
print(f"The binary value of decimal {decimal_num} is {binary_str}")
