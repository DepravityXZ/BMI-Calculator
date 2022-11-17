print("WELCOME TO THE BMI CALCULATOR!")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
calculation = weight/(height**2)
bmi = round(calculation,0)
bmi_int = int(bmi)
if bmi_int < 18.5 :
    print(f"Your BMI is {bmi_int}, you are underweight.")
elif bmi_int > 18.5 and bmi_int < 25 :
    print(f"Your BMI is {bmi_int}, you have a normal weight.")
elif bmi_int > 25 and bmi_int < 30 :
    print(f"Your BMI is {bmi_int}, you are slightly overweight.")
elif bmi_int > 30 and bmi_int < 35 :
    print(f"Your BMI is {bmi_int}, you are obese.")
else:
    bmi_int > 35 
    print(f"Your BMI is {bmi_int},you are clinically obese")