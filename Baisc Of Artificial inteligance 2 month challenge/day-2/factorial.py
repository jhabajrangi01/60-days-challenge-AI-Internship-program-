#Question:- WAP to find the factorial of a number using loop.
num = int(input("Enter any number = "))
fact = 1
for i in range(1, num):
    fact = fact * num
    num = num - 1
print("Factorial = ", fact)


#Output
"""
Enter any number = 6
Factorial =  720
"""