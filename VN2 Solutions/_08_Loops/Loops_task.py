n=11
for i in range(0,n):
    print(i)

n = 10
for i in range(n):
    if i % 2 == 0:
        print("Even", i)
    else:
        print("ODD",i)

print("==================================================================")

#Python program to calculate the sum of all numbers from 1 to a given number.
n = 10
sum = 0
for i in range(1 ,n+1):
    sum += i
print(sum)

print("==================================================================")

#Python program to print a multiplication table of a given number
n=10
for i in range(11):
    print(5,"X",i,"=",5*i)

print("===================================================================")

#Python program to count the total number of digits in a number.
n = 12857637
n =str(n)
count = 0
for i in n:
    count += 1
print(count)

print("======================================================================")

#Python program to check if the given string is a palindrome or not.
given_string = str(input())
reverse_string = ""

for i in given_string:
    reverse_string = i + reverse_string
if given_string == reverse_string:
    print("The given number",given_string,"is a Pallindrome")
else:
    print("The given number",given_string,"is not a Pallindrome")

#Python program to check if a given number is an Armstrong number
given_num = int(input("Enter the number u want to check:-"))
given_num = str(given_num)
string_length = len(given_num)
sum = 0
for i in given_num :
sum += int(i) ** string_length

if sum == int(given_num):
    print("Amstrong Number")
else:
    print("Not a Amstrong Number")

print("========================================================================")

#python program to print factorial of a number

n = int(input("Enter a number for its factorial:-"))
fact = 1
if n < 1:
    print("No factorial for negative numbers")
elif n == 0:
    print("Factorial for 0 is 1.")
else:
    for i in range(n,n+1):
        fact = fact * i
        print("The factorial of number is",fact)

print("==========================================================================")

#Write a program that calculates the average of a given list of numbers.
list1 = [21,34,55,89]
len_list1 = len(list1)
sum =0
for i in list1:
    sum = sum + i
print("The average of the numbers in list is",sum/len(list1))

print("============================================================================")

#Python program to count the number of even and odd numbers from a series of numbers.
num_list = [20,21,22,23,54,19,22,24]
even = 0
odd = 0
for i in num_list:
    if i%2 == 0:
        even += 1
    else:
        odd += 1
print(odd)
print(even)

print("==========================================================================")

#Find Maximum and Minimum:
#Write a program to find the maximum and minimum numbers in a given list.

numbers = [55, 35, 10, 12, 7, 14]
max_num = min_num = numbers[0]
for i in numbers:
    if i > max_num:
        max_num = i
    elif i < min_num:
        min_num = i
print("The maximum number is:", max_num)
print("The minimum number is:", min_num)

print("===========================================================================")

#Write a program that removes duplicates from a given list
given_list = [1, 2, 2, 3, 4, 3, 5, 6, 5]
unique_list = []
for i in given_list:
    if i not in unique_list:
        unique_list.append(i)
print("List without duplicates:", unique_list)

print("============================================================================")

# Example string and character to remove
input_string = "Hello World!"
character_to_remove = "l"
result_string = ""

for i in input_string:
    if i != character_to_remove:
              result_string = result_string + i
print(input_string)
print(result_string)

print("============================================================================")

# Write a program that reverses the order of elements in a given list.
given_list = [1, 2, 3, 4, 5]
reversed_list = []

for i in given_list[::-1] :
    reversed_list.append(i)
print("Original list:", given_list)
print("Reversed list:", reversed_list)

print("==========================================================================")

#Check Perfect Number:
#Description: Write a program to check if a given number is a perfect number.

number = int(input("Enter a number: "))
summ = 0
for i in range(1,number) :
    if number % i == 0 :
        summ = summ + i
if summ == number :
    print("Number is Perfect Number")
else :
    print("Number is not a Perfect Number")

print("==========================================================================")

'''
Password Strength Checker:
Description: Write a program that checks the strength of a password based on the following criteria:

Contains at least 8 characters
Contains at least one uppercase letter
Contains at least one lowercase letter
Contains at least one digit 
'''
while True:
    user_password = input("Enter your password: ")

    if len(user_password) < 8:
        print("Your password is weak. It should have at least 8 characters.")
    else:
        has_uppercase = False
        has_lowercase = False
        has_digit = False

        for char in user_password:
            if char.isupper():
                has_uppercase = True
            elif char.islower():
                has_lowercase = True
            elif char.isdigit():
                has_digit = True

        if not has_uppercase:
            print("Your password is weak. It should have at least one uppercase letter.")
        elif not has_lowercase:
            print("Your password is weak. It should have at least one lowercase letter.")
        elif not has_digit:
            print("Your password is weak. It should have at least one digit.")
        else:
            print("Congratulations! Your password is strong.")
            break

print("=================================================================================================")

#Count Characters in a String:
#Description: Write a program that counts the occurrences of each character in a given string.

input_string = input("Enter a string: ")

# Initialize an empty dictionary to store character counts
char_count = {}

# Iterate through each character in the input string
for char in input_string:
    # Check if the character is already in the dictionary
    # If it is, increment its count by 1
    # If it is not, add it to the dictionary with a count of 1
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)

print("=====================================================================")

#Calculate GCD:
#Description: Write a program to calculate the greatest common divisor (GCD) of two given numbers.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Swap numbers if num2 is greater than num1
if num2 > num1:
    num1, num2 = num2, num1

while num2 != 0:
    remainder = num1 % num2
    num1 = num2
    num2 = remainder

print("The GCD of the given numbers is:", num1)

print("===========================================================================")

''''
Count Words in a Sentence:
Description: Write a program that counts the number of words in a given sentence.
Example:
Input: "Hello, how are you?"
Output: 4
'''
# Get the input sentence from the user
sentence = input("Enter a sentence: ")

# Initialize a variable to store the word count
word_count = 0

# Iterate through each character in the sentence
for char in sentence:
    # If the character is a space (indicating the end of a word), increase the word count
    if char == ' ':
        word_count += 1

# Increment the word count by 1 to account for the last word in the sentence
word_count += 1

# Print the word count
print("Number of words in the sentence:", word_count)

print("=========================================================")

#Finding the common elements in a string.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Initialize an empty list to store the common elements
common_elements = []

# Iterate through each element in list1
for element in list1:
    # Check if the element is present in list2
    if element in list2:
        common_elements.append(element)

print("Common elements between the two lists:", common_elements)

print("===============================================================")

'''
Calculate Square Root:
Description: Write a program to calculate the square root of a given number using the Newton-Raphson method.
Example:
Input: 16
Output: 4.0
'''
number = float(input("Enter a number: "))
guess = number / 2  # Initial guess for the square root

# Perform iterations to improve the approximation
while abs(guess * guess - number) > 1e-6:
    guess = (guess + number / guess) / 2

print("The square root of", number, "is:", guess)

print("=================================================================")

'''
Swap Case:
Description: Write a program that swaps the case (upper to lower and vice versa) of each character in a given string.
Example:
Input: "Hello, World!"
Output: "hELLO, wORLD!"
'''
input_string = input("Enter a string: ")
output_string = ""

# Iterate through each character in the input string
for char in input_string:
    # Check if the character is uppercase, then convert it to lowercase
    if char.isupper():
        output_string += char.lower()
    # Check if the character is lowercase, then convert it to uppercase
    elif char.islower():
        output_string += char.upper()
    # If the character is neither uppercase nor lowercase, keep it unchanged
    else:
        output_string += char

print("Swapped case string:", output_string)


print("=========================================================================")

'''
Word Frequency Counter:
Description: Write a program that counts the frequency of each word in a given text.
Example:
Input: "Hello world. Hello Python. Python is awesome."
Output: {'Hello': 2, 'world': 1, 'Python': 2, 'is': 1, 'awesome': 1}
'''
input_text = input("Enter a text: ")

# Initialize an empty dictionary to store word frequencies
word_frequency = {}

# Split the input text into words using spaces as separators
words = input_text.split()

# Iterate through each word in the list of words
for word in words:
    # Remove any punctuation from the word
    word = word.strip(".,!?")
    # Convert the word to lowercase to ensure case-insensitive counting
    word = word.lower()

    # Check if the word is already in the dictionary
    # If it is, increment its count by 1
    # If it is not, add it to the dictionary with a count of 1
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("Word frequency:", word_frequency)


print("===========================================================================")

'''
Anagram Checker:
Description: Write a program that checks if two given strings are anagrams of each other.
Example:
Input: "listen", "silent"
Output: True
'''

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Remove any spaces from the strings and convert them to lowercase
string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

# Check if the lengths of the two strings are different
if len(string1) != len(string2):
    print("False")
else:
    # Initialize a dictionary to store character frequencies for string1
    char_count = {}

    # Iterate through each character in string1 and update its frequency in the dictionary
    for char in string1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Iterate through each character in string2 and decrement its frequency in the dictionary
    # If a character is not present in the dictionary or its frequency becomes zero, the strings are not anagrams
    for char in string2:
        if char in char_count and char_count[char] > 0:
            char_count[char] -= 1
        else:
            print("False")
            break
    else:
        print("True")

print("============================================================================")


'''
18.Word Frequency Counter:
Description: Write a program that counts the frequency of each word in a given text.
Example:
Input: "Hello world. Hello Python. Python is awesome."
Output: {'Hello': 2, 'world': 1, 'Python': 2, 'is': 1, 'awesome': 1}
'''
# Get the input text from the user
text = input("Enter the text: ")

# Convert the text to lowercase to ensure case-insensitivity
text = text.lower()

# Initialize an empty dictionary to store word frequencies
word_freq = {}

# Split the text into individual words
words = text.split()

# Iterate through each word in the list
for word in words:
    # Remove any punctuation from the word
    word = word.strip('.,!?:"')

    # Check if the word is already in the dictionary
    if word in word_freq:
        # If it is, increment its frequency by 1
        word_freq[word] += 1
    else:
        # If it is not, add it to the dictionary with a frequency of 1
        word_freq[word] = 1

# Print the word frequency dictionary
print("Word Frequency:", word_freq)

print("===================================================================")
'''
1.Count Characters in a String:
Description: Write a program that counts the occurrences of each character in a given string.
'''

# Input string for testing
input_string = "Hello, World!"

# Create a dictionary to store the character counts
char_count = {}

# Iterate through each character in the input string
for char in input_string:
    # If the character is already in the dictionary, increment its count
    if char in char_count:
        char_count[char] += 1
    # If the character is not in the dictionary, add it with count 1
    else:
        char_count[char] = 1

# Print the character counts
for char, count in char_count.items():
    print(f"'{char}' occurs {count} time(s) in the string.")




































