# Prints welcome message
print("<== Welcome to Green Grocers! ==>")

# Information of items for sale (at least 4 items)
items=[
    # Item name, Amount, Price, Quantity
    ["Beef short ribs", "150g", 16.99, None],
    ["Pasteurized eggs", "12 pcs", 6.99, None],
    ["Frozen tonkotsu ramen", "1 pack", 4.99, None],
    ["Brie cheese round", "8oz", 8.99, None],
    ["Bottled Oolong tea", "500mL", 1.59, None]
]

# Tells the user how many items are for sale
print(f"We have {len(items)} items for sale.")

# Line break
print()

# Loop through each item and asks the user how many they would like
for i, (item, amount, price, _) in enumerate(items):
    # Prints the item name, amount, and its price
    print(f"[{i+1}/{len(items)}] {item} --- {amount} @ ${price}")
    # Item quantity input loop
    while True:
        # Asks the user how many would they like for that specific item
        item_quantity=input("How many would you like? ")
        # Checks if the quantity is a positive integer (uses isdigit)
        if item_quantity.isdigit():
            # Converts the string item quantity to an integer
            item_quantity=int(item_quantity)
            # Exits the input loop
            break
        else:
            # Tells the user the item quantity they enter is invalid
            print("Please enter a valid number of items to purchase.")
    # Add to item quantity list
    items[i][3]=item_quantity
    # Line break
    print()

# Calculate subtotal
subtotal=0
# Iterate through the items array
for _, _, price, quantity in items:
    # Adding each item's subtotal to the total subtotal
    subtotal+=price*quantity
# Calculate the tax (Ontario)
tax=subtotal*0.13
# Calculate the grand total
grand_total=subtotal+tax

# Print the calculations as receipts
print("<== Receipt ==>")
# Outputs the subtotal
print(f"Subtotal: ${subtotal:.2f}")
# Outputs the tax
print(f"Tax: ${tax:.2f}")
# Outputs the grand total
print(f"Grand total: ${grand_total:.2f}")

# Line break
print()

# Payment method input loop
while True:
    # Gets the payment method from the user
    payment_method=input("How would you like to pay (cash, debit, credit)? ")
    # Checks if the payment method the user entered is on of the three (uses if elif else)
    if payment_method=="cash":
        # Exits the input loop
        break
    # Checks if the payment method is valid
    elif payment_method=="debit":
        # Exits the input loop
        break
    # Checks if the payment method is valid
    elif payment_method=="credit":
        # Exits the input loop
        break
    else:
        # Tells the user the payment method is invalid
        print("Please enter a valid payment method. ")

# Line break
print()

# Output payment method message
print(f"You paid ${grand_total:.2f} by {payment_method}.")
# Thanking the user for shopping in green grocers
print("Thank you for shopping at Green Grocers!")
