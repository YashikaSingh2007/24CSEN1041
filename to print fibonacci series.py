terms = int(input("Enter the number of terms (greater than 2): "))
f1 = 0
f2 = 1
f3 = f1 + f2

print("Fibonacci Series:")
print(f1)
print(f2)

i = 3
while True:
    print(f3)
    f1 = f2
    f2 = f3
    f3 = f1 + f2
    i += 1
    if i > terms:
        break


# OUTPUT:
Enter the number of terms (greater than 2): 5
Fibonacci Series:
0
1
1
2
3


