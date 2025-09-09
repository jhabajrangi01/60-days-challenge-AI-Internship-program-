#Question:- WAP to print the Fibonacci sequence up to n terms.
num = int(input("Enter any number = "))
a = 0
b = 1
print("Fibonacci sequence up to n terms.")

for i in range(0, num):
    c = a + b
    b = a
    a = c
    print(c)


#Output
"""
Enter any number = 15
Fibonacci sequence up to n terms.
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
"""

