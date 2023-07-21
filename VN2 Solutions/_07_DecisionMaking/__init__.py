'''
#EVEN ODD
Analysis:
==================
    Functional Analysis:
        1. Customer will give number
        2. Check whether it is even or odd
        3. Print it accordingly
    Technical Analysis:
        STATE   : int
        Behavior: Operators, DM,          _08_Loops
                  % ==       if else
'''
print("Checking even or odd")
n=int(input("Enter number:"))
if (n%2==0):
    print("Number is even",n)
else:
   print("Number is odd ",n)

print("===================================================")

'''
Analysis:
   ==================
       Functional Analysis:
           1. Customer will give marks
           2. Check whether it is fail or pass
           3. Print it accordingly
       Technical Analysis:
           STATE   : int
           Behavior: Operators, DM,          _08_Loops
                     % ==       if else

'''
marks=int(input("Enter your marks out of 100:-"))
if (marks>33):
    print("Student is pass")
else:
    print("Student is fail")

print("==================================================")

'''
Analysis:
=================
       Functional Analysis:
           1. Customer will give numbers
           2. Check whether it is zero ,negative ,positive
           3. Print it accordingly
       Technical Analysis:
           STATE   : int
           Behavior: Operators, DM,          _08_Loops
                     > ==       if elif else

'''
n=int(input("Enter the numbers :"))
if(n>0):
    print("positive number")
elif(n==0):
    print("zero number")
else:
    print("negative number")

print("=====================================================")

'''
Analysis:
=================
           Functional Analysis:
               1. Customer will give number
               2. Check whether it is smaller or not
               3. Print it accordingly
           Technical Analysis:
               STATE   : int
               Behavior: Operators, DM,          _08_Loops
                         < ==       if elif else

'''
i = 10
if (i == 10):
    if (i < 15):
        print("i is smaller than 15")

    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")

print("==================================================")

''' 
Analysis:
=============
          Functional Analysis:
              1. Customer will give age
              2. Check whether it is adult or teenager
              3. Print it accordingly
          Technical Analysis:
              STATE   : int
              Behavior: Operators, DM,          _08_Loops
                        >      if  else

'''
age=int(input("Enter an age : "))
if( age < 18):
   print(" You are a minor ")
elif( age<=65 ):
   print("You are an adult")
else:
    print("You are a senior citizen")

print("==================================================")

'''
Analysis:
==============
          Functional Analysis:
              1. Customer will give percentage 
              2. Check whether which grade is assign
              3. Print it accordingly
          Technical Analysis:
              STATE   : int
              Behavior: Operators, DM,          _08_Loops
                        >=      if elif  else
'''

percentage =float(input("Enter percentage:"))
if(percentage>=90):
   print("Assign grade A ")
elif(percentage>=75):
   print("Assign grade B ")
elif(percentage>=65):
   print("Assign grade C ")
else:
   print("Assign grade D ")

print("================================================")

'''
Analysis:
=================
                  Functional Analysis:
                      1. score will give admission
                      2. Check whether it is win or loss
                      3. Print it accordingly
                  Technical Analysis:
                      STATE   : int
                      Behavior: Operators, DM,          _08_Loops
                                > <     if elif  

              '''

score = int(input("Input the score you got:-"))
if (score>33):
    print("Your score is",score,",so you will get Admission")
elif(score<33):
    print("Your score is",score,",will not be able to get Admission.Better luck next time!!!")

print("============================================================")

'''
Task:4 ; Complex Decision Making
Description: Ask students to create a program that simulates a simple quiz.
The program should present a series of multiple-choice questions to the user and keep track of their score. 
At the end of the quiz, display the user's score as a percentage.
'''
print("Quiz")
score=0
print("1.what is ......?")
print(" 1.abc 2.xyz 3.mno 4.pqr")
ans1=int(input("ans: "))
if ans1==1:
    score+=1
# print(score)
print("2.what is ......?")
print(" 1.abc 2.xyz 3.mno 4.pqr")
ans2=int(input("ans: "))
if ans2==3:
    score+=1
# print(score)
print("3.what is ......?")
print(" 1.abc 2.xyz 3.mno 4.pqr")
ans3=int(input("ans: "))
if ans3==2:
    score+=1
# print(score)
print("4.what is ......?")
print(" 1.abc 2.xyz 3.mno 4.pqr")
ans4=int(input("ans: "))
if ans4==2:
    score+=1
print("total percentage is: ",(score/4)*100)

print("========================================================")

'''
Task:5; Decision Making with _08_Loops
Description: Have students create a program that generates a random number between 1 and 100.
The user should guess the number, and the program should provide feedback on whether the guess is too high or too low. 
The program should continue until the user guesses the correct number.
'''
# Task :6 ;Calculate the sum of three given numbers, if the values are equal then return thrice of their sum
num1 = int(input("Enter the first number :-"))
num2 = int(input("Enter the second number:-"))
num3 = int(input("Enter the third number :-"))
sum = num1+num2+num3
print("Sum of the number is:-",sum)
if (num1==num2==num3):
    print(3*sum)

print("==============================================")

'''
Task 11: Leap Year Checker
Description: Create a program that checks if a given year is a leap year or not.
Example Input: 2024
Example Output: "2024 is a leap year."
'''
print("If a given year is a leap year or not")
year = int(input("Enter a year:-"))
if (year%4==0):
    print("This is a leap year")
else:
    print("This is not a leap year")

print("====================================================")

'''
Task 13: BMI Calculator
Description: Create a program that calculates a person's Body Mass Index (BMI) based on their height and weight.
Example Input: Height = 1.75m, Weight = 68kg
Example Output: "Your BMI is 22.2."
'''
print("BMI Calculator")
height = float(input("Enter your height(in m):-"))
weight = float(input("Enter your weight(in kg):-"))
bmi = weight/(height)**2
print("Your BMI is:-",bmi)

print("=======================================================")

'''
Task:3 ; Nested Conditional Statements
Description: In this task, students should develop a program that calculates the discount amount for a shopping cart 
based on the following conditions:

If the total price is greater than or equal to $100, apply a 10% discount.
If the total price is between $50 and $99.99, apply a 5% discount.
If the total price is less than $50, no discount is applied.

Analysis:
==================
                  Functional Analysis:
                      1. Develop a program that calculates the discount amount
                      2. Checks the discount amount. 
                      3. Print it accordingly
                  Technical Analysis:
                      STATE   : int
                      Behavior: Operators, DM,          _08_Loops
                                > < =     if elif else 
'''
print("Calculate discount")
amount = float(input("Enter the Total Amount:-"))
if (amount>50):
    print("Discount is available!!!")
if (amount>=99.99):
    dis = (10 / 100 * amount)
    print("Customer got Rs.",dis, "discount")

elif(amount>=50):
    dis = (5 / 100 * amount)
    print("Customer got Rs.",dis, "discount!!!")
else:
    print("No discount is Available...")

print("===========================================================")

'''
Task 16: User Authentication
Description: Create a program that verifies a user's login credentials (e.g., username and password).
Example Input: Username = "john_doe", Password = "pass123"
Example Output: "Login successful."
'''
print("User Authentication")
username = input("USERNAME:-")
if username == "sohit123":
    print("Username is correct")
    password = input("PASSWORD")
    if password == "123456":
        print("Login Successfully")
    else:
        print("Incorrect password!!! /n LOGIN FAILED")
else:
    print("Username is incorrect")

print("=================================================================================================")
'''
Task 19: Email Validation
Description: Create a program that validates if a given email address is correctly formatted.
Example Input: "john.doe@example.com"
Example Output: "The email address is valid." 
'''
print("Email validation")
user = input("Enter Email Address:-")
if user.endswith("@gmail.com"):
    print("Valid Email Address")
else:
    print("Email not valid")

print("======================================================================================================")
'''
Task:5; Decision Making with _08_Loops
Description: Have students create a program that generates a random number between 1 and 100. The user should guess the number,
and the program should provide feedback on whether the guess is too high or too low. The program should 
continue until the user guesses the correct number.
'''
import random
user_input = int(input("Guess the number: "))
num = random.randint(1, 100)
while  user_input <=100 and user_input >=0:
    if user_input >= 0 and user_input <= 100:
        print("Entered a valid number")
        if user_input == num:
            print("Congratulations, you won")
            break
        elif user_input > num:
            print("Entered number is too high")
            user_input = int(input("Enter the number again: "))
        elif user_input < num:
            print("Entered number is too low")
            user_input = int(input("Enter the number again: "))
    else:
        print("Please Enter the number between 1 to 100")
        user_input = int(input("Enter the number again: "))

print("=============================================================================")

#Task : 9 : Python program to test whether a passed letter is a vowel or not.
print("Checking Vowel")
vowel1 = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
letter = input("Enter any letter:")
if letter in vowel1:
    print("Your letter is a vowel")
else:
    print("Your letter is not a vowel")

print("==============================================================================")
'''
Task 15: Temperature Converter
Description: Write a program that converts a given temperature from Celsius to Fahrenheit or vice versa.
'''
print("Degree Celsius to Fahrenheit")
temp = float(input("Enter temperature in Celsius:-"))
fahrenheit = (temp * 9/5) + 32
print(fahrenheit)

print("=================================================================================")

'''
Task 21: Rock, Paper, Scissors Game
Description: Write a program that allows two players to play the classic game of rock, paper, scissors and determines the winner.
Example Input: Player 1: "rock", Player 2: "scissors"
Example Output: "Player 1 wins!"
'''
player1 = input("Player 1 :- Select Rock, Paper, or Scissor:-").lower()
player2 = input("Player 2 :- Select Rock, Paper, or Scissor:-").lower()
print("Player1:", player1)
print("Player2:", player2)
if player1 == "rock" and player2 == "paper":
    print("Player 2 WON!!!")
elif player1 == "paper" and player2 == "scissor":
    print("Player 2 WON!!!")
elif player1 == "scissor" and player2 == "rock":
    print("Player 2 WON!!!")
elif player1 == player2:
    print("TIE IT IS!!!")

print("==========================================================================================")

'''
Task 22: Currency Converter
Description: Create a program that converts an amount of money from one currency to another based on current exchange rates.
'''
print("Currency Converter")
convert = int(input("Enter the currency you want to convert(in USD):-"))
convert = convert * 0.90
print(convert)

print("==========================================================================================")

'''
Task 23: Password Strength Checker
Description: Develop a program that evaluates the strength of a user's password based on certain criteria 
(e.g., length, complexity).
Example Input: "Pa$$w0rd"
Example Output: "The password is strong."
'''
user_password = input("Enter your password: ")

has_uppercase = any(char.isupper() for char in user_password)
has_lowercase = any(char.islower() for char in user_password)
has_digit = any(char.isdigit() for char in user_password)
has_special_char = any(char in "!@#$%^&*(),.?\":{}|<>" for char in user_password)

if len(user_password) < 8:
    print("Your password is weak. It should have at least 8 characters.")
elif not has_uppercase:
    print("Your password is weak. It should have at least one uppercase letter.")
elif not has_lowercase:
    print("Your password is weak. It should have at least one lowercase letter.")
elif not has_digit:
    print("Your password is weak. It should have at least one digit.")
elif not has_special_char:
    print("Your password is weak. It should have at least one special character.")
else:
    print("Your password is strong.")


print("================================================================================================")
'''
Task 20: Number System Converter
Description: Develop a program that converts a given number from one number system to another (e.g., binary to decimal).
Example Input: Binary number = "10101"
Example Output: "The decimal equivalent is 21."
'''
l = ["xyz","abc","bca"]
for i in l:
    print

for i in range(1,2) :
    for j in range(1, 2):
        print(i, j)

for i in range(0, 10, 2):
	print(i)

for i in range(0, 10, 2):
    print(i)

binary = (input("Enter a binary number : "))
decimal = 0
for i in range(len(binary)):
    decimal += int((binary[len(binary)-i-1]))*(2**i)
    print(decimal)

t = ((1, 2), (3, 4), (5, 6))
for a, b in t:
	print(a, b)













