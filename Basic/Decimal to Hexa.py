def decimal_to_hexadecimal(decimal_num):
    if decimal_num == 0:
        return '0'
    
    hex_str = ''
    hex_chars = '0123456789ABCDEF'
    
    while decimal_num > 0:
        hex_str = hex_chars[decimal_num % 16] + hex_str
        decimal_num = decimal_num // 16
    
    return hex_str

decimal_num = int(input("Enter the number in decimal: "))
hex_str = decimal_to_hexadecimal(decimal_num)
print(f"The hexadecimal value of decimal {decimal_num} is {hex_str}")
