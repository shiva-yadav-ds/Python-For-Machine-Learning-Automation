user_age = input("Enter your current age : ")
age_as_int = int(user_age)
year_remaining = 90 - age_as_int
days_remaining = year_remaining * 365
months_remaining = year_remaining * 12
weeks_remaining = days_remaining // 7 
print(f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left" )