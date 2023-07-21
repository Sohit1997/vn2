"""
Caesar Cipher:
Description: Write a program that encrypts a given string using the Caesar cipher technique.
Example:
Input: "Hello", shift=3
Output: "Khoor"
"""
input_str = "hello"
print(input_str)
output_str = ""
capital ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small = 'abcdefghijklmnopqrstuvwxyz'

for i in input_str:

    if i in small:
        output_str += chr(ord(i) - 29)
    elif i in capital:
        output_str += chr(ord(i) + 35)
    else:
        output_str += " "

print(output_str)