print("Welcome to the rollerroaster!")
height = int(input("What is your height in cm? : "))
bill = 0

if height >= 120:
  print("you can ride the rollarcoaster!")
  age = int(input("What is your age? : "))
  if age < 12:
    bill = 50
    print("Child ticket are 50rs")
  elif 12<= age <= 18:
    bill = 80
    print("Youth ticket are 80rs")  
  else :
    bill = 110
    print("Adult ticket are 110rs")

  wants_photo = input("Do you want to photo take? y or n. : ")
  if wants_photo == "y":
    print(f"Now have to pay {bill}+10 = {bill+10}")
  else:
    print(f"you have to pay only {bill}")  

else:
  print("Sorry, you have grow taller before you can ride.")  