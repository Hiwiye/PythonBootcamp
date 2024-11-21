weight = float(input("what is your weight in kg?"))
height = float(input("what is your height in m?"))
BMI = weight/height ** 2
print("Your BMI is", BMI ) 
if BMI < 18.5:
    print("underweight")
elif BMI < 25:
    print("normal weight")
else:
    print("over weight")
