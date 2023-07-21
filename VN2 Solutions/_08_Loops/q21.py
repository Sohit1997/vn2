"""
Task 20: Number System Converter
Description: Develop a program that converts a given number from one number system to another (e.g., binary to decimal).
Example Input: Binary number = "10101"
Example Output: "The decimal equivalent is 21.
"""
number_system = "binary"
number = "10101"

if number_system == "binary":
  decimal_equivalent = int(number, 2)
elif number_system == "decimal":
  decimal_equivalent = int(number)
elif number_system == "octal":
  decimal_equivalent = int(number, 8)
elif number_system == "hexadecimal":
  decimal_equivalent = int(number, 16)
else:
  raise ValueError(f"Invalid number system: {number_system}")

print(f"The decimal equivalent is {decimal_equivalent}")
