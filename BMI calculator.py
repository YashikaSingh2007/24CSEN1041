def calculate_bmi(weight,height):
    bmi = weight/(height**2)
    return bmi
weight = float(input("Enter the weight:"))
height = float(input("Enter the height:"))

bmi = calculate_bmi(weight,height)
print(f"Your BMI is: {bmi: .2f}")
