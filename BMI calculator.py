def calculate_bmi(weight,height):
    bmi = weight/(height**2)
    return bmi
weight = float(input("Enter the weight:"))
height = float(input("Enter the height:"))

bmi = calculate_bmi(weight,height)
print(f"Your BMI is: {bmi: .2f}")



OUTPUT:
Enter the weight:70.0
Enter the height:1.75
Your BMI is:  22.86

Enter the weight:50.5
Enter the height:1.65
Your BMI is:  18.55

