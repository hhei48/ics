# Import the math library
import math
# Import dedent for styling
from textwrap import dedent

# Print the title and the menu of options
print(dedent("""
    <== Magical Math Methods ==>

    < Menu of Options >
    1) Convert the first number from degrees to radians
    2) Calculate the first number to the power of the second number
    3) Print the first number rounded down to the nearest integer
    4) Print the first number rounded up to the nearest integer
    5) Calculate the square root of the first number
"""))

# Enter error loop
while True:
    # Error handling
    try:
        # Try if you can convert the input choice to integers
        choice=int(input("Please select your choice: "))
    # Cannot convert to integer
    except ValueError:
        # Print error message
        print("Error: Please enter a valid choice")
        # Adds an extra line for styling
        print()
        # Go back to the start
        continue
    # Check if the choice is within the menu range
    if(1<=choice<=5):
        # Break out of error loop if valid
        break
    # Invalid choice
    else:
        # Error message
        print("Error: Please enter a valid choice")
        # Prints and extra line styling
        print()

# Prints and extra line styling
print()

# Enter error loop
while True:
    # Error handling
    try:
        # Get the 2 numbers from user
        x,y=input("Please enter 2 numbers: ").split()
        # Convert to float
        x=float(x)
        # Convert second number to float
        y=float(y)
        # Break out of error loop if nothing happens
        break
    # Something happened
    except ValueError:
        # Prints error message
        print("Error: Please enter valid numbers")
        # Extra line for style
        print()

# Prints the result
print("Result: ", end="")
# See which choice the user chose
match choice:
    # User chose option 1
    case 1:
        # Converts from degree to radians
        print(f"{math.radians(x):.2f}")
    # User chose option 2
    case 2:
        # Calculate power using the first and second number
        print(f"{math.pow(x, y):.2f}")
    # User chose option 3
    case 3:
        # Round down number
        print(f"{math.floor(x):.0f}")
    # User chose option 4
    case 4:
        # Round up number
        print(f"{math.ceil(x):.0f}")
    # User chose option 5
    case 5:
        # Calculate square root
        print(f"{math.sqrt(x):.2f}")
