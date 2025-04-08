"""BMI Calculator"""

weight = 85
height = 1.85

bmi = weight / (height**2)

if bmi < 18.5:
    print("underweight")
elif bmi < 25 and bmi >= 18.5:
    print("normal weight")
else:
    print("overweight")
