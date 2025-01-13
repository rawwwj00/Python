def hexadecimal_to_decimal(hex_str):
    decimal = 0
    power = 0
    
    for digit in reversed(hex_str):
        if '0' <= digit <= '9':
            decimal += int(digit) * (16 ** power)
        elif 'A' <= digit <= 'F':
            decimal += (ord(digit) - ord('A') + 10) * (16 ** power)
        elif 'a' <= digit <= 'f':
            decimal += (ord(digit) - ord('a') + 10) * (16 ** power)
        power += 1
    
    return decimal

# Example usage
hex_str =input("Enter the number in Hexa-Decimal: ")
decimal_value = hexadecimal_to_decimal(hex_str)
print(f"The decimal value of hexadecimal {hex_str} is {decimal_value}")
