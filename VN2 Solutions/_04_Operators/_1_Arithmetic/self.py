print("Percentage of student")
math=50
sci= 40
hin= 70
eng= 80
percent = (math+sci+hin+eng)/400 *100
print(percent)
print("=================================================")


print("FIND ODD OR EVEN")
num = int(input("Enter a number:"))
if (num%2==0):
      print("Even")
else:
     print("Odd")

print("=================================================")

#1.)REVESING A NUMBER USING WHILE LOOP

num = int(input("Enter a number you want to reverse :-"))
reverse =0
while num!=0:
    reverse = reverse*10 + num%10
    num =num//10
print("reveresed string is ",reverse)

#2.)REVESRING A NUMBER USING SLICING

num = int(input("Enter a number:-"))
reverse = int(str(num)[::-1])
print(reverse)


def factorial(x):
    if x==1 :
        return 1
    else :
        return (x*factorial(x+1))
num =7
result = factorial(num)
print("The factorial of", num, "is", result)


























































































