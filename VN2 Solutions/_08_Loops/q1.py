"""Count Characters in a String:
Description: Write a program that counts the occurrences of each character in a given string.
Example:
Input: "hello"
Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}"""

string= input("enter a string: ")
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)



