"""Find Maximum and Minimum:
Description: Write a program to find the maximum and minimum numbers in a given list.
Example:
Input: [4, 9, 2, 7, 5]
Output: Maximum: 9, Minimum: 2"""

list= [4,9,2,7,5]
max_num=list[0]
min_num=list[0]
for num in  list:
    if max_num<num:
        max_num = num
    if num < min_num:
         min_num = num
print("max num is ",max_num)
print("The smallest number is:",min_num)
