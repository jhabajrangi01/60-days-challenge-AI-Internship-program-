#Question:- Create a simple calculator (add, sub, mul, div) using if-else.
num1 = int(input("Enter first number = "))
num2 = int(input("Enter second number = "))

print("Calculator Create")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice(1-4) = "))

if choice==1:
    num3 = num1 + num2
    print("Sum = ",num3)
elif choice==2:
    num3 = num1 - num2
    print("Difference = ",num3)
elif  choice==3:
    num3 = num1 * num2
    print("Product = ",num3)
elif choice==4:
    num3 = num1 / num2
    print("Quotient = ",num3)
else:
    print("Invalid Choice")


#Output:-  
"""
1. Enter first number = 15
Enter second number = 10
Calculator Create
1. Addition
2. Substraction
3. Multiplication
4. Division
Enter your choice(1-4) = 3
Sum =  25

2. Enter first number = 15
Enter second number = 10
Calculator Create
1. Addition
2. Substraction
3. Multiplication
4. Division
Enter your choice(1-4) = 2
Difference =  5

3. Enter first number = 15
Enter second number = 10
Calculator Create
1. Addition
2. Substraction
3. Multiplication
4. Division
Enter your choice(1-4) = 3
Product =  150

4. Enter first number = 15
Enter second number = 10
Calculator Create
1. Addition
2. Substraction
3. Multiplication
4. Division
Enter your choice(1-4) = 4
Quotient =  1.5
"""