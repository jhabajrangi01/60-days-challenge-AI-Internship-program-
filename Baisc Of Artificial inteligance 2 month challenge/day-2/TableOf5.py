#Question:- Print multiplication table of 5 using while loop.
i = 1
table = int(input("Enter table number = "))
#i = 1

while i <= 10:
    print(f"{table} X {i} = {table * i}")
    i = i + 1

#Output
"""
Enter table number = 5
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
"""