#Question:- Print all odd numbers between 1 and 50.
sum = 0
print("Odd number between 1 to 50:")
for i in range(1, 50):
    if i % 2 != 0:
        sum = sum + i
        print(i)

print("Sum of all odd num between 1 to 50 = ",sum)


#Output
"""
Odd number between 1 to 50:
1
3 
5 
7 
9 
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
Sum of all odd num between 1 to 50 = 625
"""