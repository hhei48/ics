# Prints the welcome message
print("<== Welcome to Putrid Pizza! ==>")

# Line break
print()

# Diameter input loop
while True:
    # Inputs the diameter as a string
    diameter=input("How big do you want your pizza to be? (diameter in cm): ")
    # Checks if the diameter is an integer AND it is bigger or equal to 1cm
    if diameter.isdigit() and int(diameter)>=1:
        # Casts the valid diameter from a string to an integer
        diameter=int(diameter)
        # Exits the input loop
        break
    else:
        # Tells the user the diameter is invalid
        print("Please enter a valid diameter.")

# Line break
print()

# Output a fun comment base on the diameter of the pizza
# If the diameter of the pizza is from 1 cm to 15 cm
if 1<=diameter<=15:
    print("We are going to make you a cute little pizza!")
# This is an additional case
elif 15<diameter<20:
    print("Perfect for a snack!")
# If the diameter of the pizza is greater than 20 cm but less than 40 cm
elif 20<=diameter<40:
    print("This will be delicious!")
# If the diameter of the pizza is greater than 40 cm
else:
    print("Whoa, big pizza! You might need a truck to get this home!")

# Line break
print()

# Calculate the pizza ingredient cost
ingredients_cost=0.5*diameter
# Calculate the pizza's fixed costs
fixed_cost=0.75+0.99
# Calculate the pizza's cost before tax
subtotal=fixed_cost+ingredients_cost

# Calculate the tax (Ontario)
tax=0.13*subtotal
# Calculate the grand total
grand_total=subtotal+tax

# Print the receipt
print("<== Receipt ==>")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${grand_total:.2f}")

# Line break
print()

# Print a thank you message to the user
print("Thank you for dining with us!")
