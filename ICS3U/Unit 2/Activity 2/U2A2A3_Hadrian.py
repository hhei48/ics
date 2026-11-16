# Print the program title
print("<== Power Calculator ==>")
# Print an extra line for styling
print()

# A function for getting integer input
def get_int_input(prompt)->int:
    # Enter error loop
    while True:
        # Try if converting the input to integer is possible
        try:
            # Get an input using the prompt
            number=int(input(prompt))
            # Return the integer
            return number
        # The entered value is not an integer
        except ValueError:
            # The error message
            print("Error: Please enter an integer")
            # Print an extra line for styling
            print()

# A function for printing the menu of options
def print_ask_menu()->int:
    # Prints the menu of options with styling
    print("Menu of Options")
    print("1... Find the value of a number squared")
    print("2... Find the value of a number cubed")
    print("3... Find the value of a number, to any power")
    print("4... Exit")
    print()
    # Enter error loop
    while True:
        # Get a valid integer input using the prompt
        choice=get_int_input("Please enter an option: ")
        # Check if the choice is valid
        if(1<=choice<=4):
            # Print an extra line for styling
            print()
            # Return the valid choice
            return choice
        # The choice is invalid
        else:
            # Prints the error message
            print("Error: Please enter a valid option")
            # Add
            print()

# A function for raising exponents
def expo(power, power_name):
    # Get the base using the prompt
    base=get_int_input(f"Please enter a number to be {power_name}: ")
    # If the provided power is not option 1 or 2
    if not(power==2 or power==3):
        # Get the power from the user
        power=get_int_input("Please enter the power: ")
        # Edit the power output message
        power_name=f"{power_name} {power}"
    # Print the output message
    print(f"The value of {base} {power_name} is {base**power}.")
    # Print an extra line for styling
    print()

# Enter the input loop
while True:
    # Print the menu and ask for the menu choice
    choice=print_ask_menu()
    # Check which choice the user selected
    match choice:
        # Option 1
        case 1:
            # Process the exponent
            expo(2, "squared")
        # Option 2
        case 2:
            # Process the exponent
            expo(3, "cubed")
        # Option 3
        case 3:
            # Process the exponent
            expo(-1, "raised to the power of")
        # Option 4
        case 4:
            # Break out of the loop to exit
            break
        # Should not be possible to reach but just in case
        case _:
            # Error message
            print("Error: Please enter a valid option")
            # Prints extra line for styling
            print()
