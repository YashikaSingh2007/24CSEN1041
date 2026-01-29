signal = input("Enter traffic signal color (red / yellow / green): ").lower()

if signal == "red":
    print("STOP")
elif signal == "yellow":
    print("GET READY")
elif signal == "green":
    print("GO")
else:
    print("Invalid signal color")


# OUTPUT:
Enter traffic signal color (red / yellow / green): yellow
GET READY

Enter traffic signal color (red / yellow / green): red
STOP




