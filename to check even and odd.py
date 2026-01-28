x= int(input("Enter an integer (positive or negative): "))

if x > 0:
    print(x,"is positive")
    if x % 2 == 0:
        print(x,"is even")
    else:
        print(x,"is odd")
elif x < 0:
    print(x,"is negative")
else:
    print(x,"is zero")


# OUTPUT:
1. Enter an integer (positive or negative): -8
-8 is negative

2.Enter an integer (positive or negative): 9
9 is positive
9 is odd

3.Enter an integer (positive or negative): 4
4 is positive
4 is even


