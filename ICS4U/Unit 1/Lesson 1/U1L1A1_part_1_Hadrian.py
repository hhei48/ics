# Prints the welcome message to the bank
print("<== Welcome to the CyberBank ==>\n")

# Error loop for handling the deposit
while True:
    # Try to input the deposity
    try:
        # Input the deposit and convert to integer
        deposit=int(input("How much would you like to deposit? $"))
    # Deposit is not an integer
    except ValueError:
        # Prints the error message for the non-integer deposit
        print("Please enter a valid integer.\n")
        # Restart the error loop
        continue
    # Check if the deposit is positive
    if deposit<=0:
        # Tell the user non-positive deposit is invalid
        print("Error: Please enter a valid amount.\n")
    # Deposit is positive
    else:
        # Can exit the error loop because everything is valid
        break

# Tell the user the CyberBank's interest rate
print("\nYour account has a 4% annual interest rate.")
# Output the current balance with 2 decimal places
print(f"Your current balance: ${deposit:.2f}\n")
# Calculate the 1 year annual interest total and output with 2 decimal places
print(f"After 1 year: ${deposit*(1.04)**1:.2f}")
# Calculate the 5 year annual interest total and output with 2 decimal places
print(f"After 5 year: ${deposit*(1.04)**5:.2f}")
# Calculate the 20 year annual interest total and output with 2 decimal places
print(f"After 20 year: ${deposit*(1.04)**20:.2f}")
# Print thank you message
print("\nThank you for banking with us today.")
