#Question:- Take a number input and print whether it is even or odd.
num = int(input("Enter any number = "))

if num%2 == 0:
    if num == 0:
        print("Given number is zero")
    else:   
        print("Given number is even")

else:
    print("Given number is odd")


#Output
"""
1. Enter any number = 0
Given number is zero

2. Enter any number = 10
Given number is even

3.Enter any number = 15
Given number is odd
"""