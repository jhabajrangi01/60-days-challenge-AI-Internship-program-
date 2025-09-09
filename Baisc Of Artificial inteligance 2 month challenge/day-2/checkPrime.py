#WAP to check if a number is prime or not.
num = int(input("Enter any number = "))

for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not Prime number")
        break
else:
    print(f"{num} is prime number")


#Output
"""
1. Enter any number = 15
15 is not Prime number

2. Enter any number = 7
7 is prime number
"""