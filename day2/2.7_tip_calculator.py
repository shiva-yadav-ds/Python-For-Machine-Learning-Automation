total_bill = int(input("What was the total bill ? ₹"))
tip = int(input("What percentage tip Wuold you like to give ? 10, 12, or 15 ? "))
tip_bill = total_bill / 10 + total_bill
split_bill = int(input("How many people to split the bill ? "))
final_payment = round(tip_bill / split_bill)
print(f"Each person should pay: ₹{final_payment}") 
