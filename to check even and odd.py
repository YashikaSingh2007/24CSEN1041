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
