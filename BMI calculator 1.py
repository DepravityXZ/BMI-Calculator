# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_new = float(height)
weight_new = float(weight)
bmi = weight_new / height_new**2
bmi_new = round(bmi)
print(bmi_new)
#print(bmi)