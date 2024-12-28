print("Welcome to Python Pizza Delivery!")
size = input("What size pizza do you want? \nSmall pizza: 20rs Type - s\nMedium Pizza: 30rs Type - m\nLarge Pizza: 35rs Type - l\nType here : ").lower()

# Base prices
price = 0
if size == "s":
    price = 20
    print("You choose Small Pizza: 20rs\nPepperoni for Small Pizza: +2rs")
elif size == "m":
    price = 30
    print("You choose Medium Pizza: 30rs\nPepperoni for Medium or Large Pizza: +3rs")
elif size == "l":
    price = 35
    print("You choose Large Pizza: 35rs\nPepperoni for Medium or Large Pizza: +3rs")
else:
    print("Invalid size selected!")
    exit()

# Ask for pepperoni
pepperoni = input("Do you want pepperoni? Type y | n: ").lower()
if pepperoni == "y":
    if size == "s":
        price += 2
    else:
        price += 3

# Ask for extra cheese
extra_cheese = input("Extra cheese for any size pizza: +3rs, Type y | n: ").lower()
if extra_cheese == "y":
    price += 3

print(f"Your final payment is {price}rs")
