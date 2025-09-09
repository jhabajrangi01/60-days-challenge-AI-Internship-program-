#Question:- WAP to find the largest of 3 numbers using if-else.
num1 = int(input("Enter first number = "))
num2 = int(input("Enter second number = "))
num3 = int(input("Enter third number = "))

if num1 > num2 and num1 > num3:
    print("First number is greater")

elif num2 >num1 and num2 > num3:
    print("Second number is greater")

else:
    print("Third number is grater")

#Output
"""
1. Enter first number = 15
Enter second number = 20
Enter third number = 12
Second number is greater


2.Enter first number = 10
Enter second number = 5
Enter third number = 36
Third number is grater

3.Enter first number = 50
Enter second number = 12
Enter third number = 31
First number is greater
"""

    