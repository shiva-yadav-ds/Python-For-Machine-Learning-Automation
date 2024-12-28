weight = int(input("Enter your Weight in kg : "))
height = float(input("Enter your Height in Meter : "))
heightx2 = height*height
bmi = round(weight/heightx2)

if bmi < 18.5 :
  print(f"Your BMI is {bmi}, you are underweight")
elif 18.5 <= bmi <= 25 :
  print(f"Your BMI is {bmi}, your weight is normal")  
elif 25 < bmi <= 30 :
  print(f"Your BMI is {bmi}, you are overweight")
elif 30 < bmi <= 35 :
  print(f"Your BMI is {bmi}, you are obese")
else :
  print(f"Your BMI is {bmi}, you are clinically obese")      