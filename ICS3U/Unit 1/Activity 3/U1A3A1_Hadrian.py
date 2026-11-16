amount=float(input("Please enter the amount spent: $"))
print()
discount_rate=-1 #not percentage
if(amount<=40):
    discount_rate=0.1
elif(amount<=80):
    discount_rate=0.2
elif(amount<=120):
    discount_rate=0.3
else:
    discount_rate=0.4
saving_percent=int(discount_rate*100)
saving_amount=round(amount*discount_rate, 2)
grand_total=round(amount*(1-discount_rate), 2)
print(f"You spent: ${amount:.2f}")
print(f"You are saving {saving_percent}%")
print(f"You are saving ${saving_amount:.2f}")
print(f"Your total is ${grand_total:.2f}")
