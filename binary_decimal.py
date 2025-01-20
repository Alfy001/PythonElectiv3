binary_number = input("Enter a binary number: ")
decimal_value = 0
exponent = 0

for bit in binary_number[::-1]:  
    decimal_value += int(bit) * (2 ** exponent)
    exponent += 1

print("The decimal equivalent of", binary_number, "is", decimal_value)
