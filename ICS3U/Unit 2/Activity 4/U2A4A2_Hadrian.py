# Import the math library
import math
# Import dedent for styling
from textwrap import dedent

# The function for option 1
def option_1():
    # Ask the user to input a string
    str=input("Please enter a string: ")
    # Output the length
    print(f"Result: {len(str)}")

# The function for option 2
def option_2():
    # Ask the user to input a string
    str=input("Please enter a string: ")
    # Output all caps string
    print(f"Result: {str.upper()}")

# The function for option 3
def option_3():
    # Enter error loop
    while True:
        # Get the string from the user
        str=input("Please enter >=4 character string: ")
        # Check if the string is long enough
        if(len(str)>=4):
            # Print the letter at the 4th position
            print(f"Result: {str[3]}")
            # Exit function
            return
        # The string is to short
        else:
            # Prints error message
            print("Error: String is too short")
            # Add an extra line for styling
            print()

# The function for option 4
def option_4():
    # Gets the first string
    str1=input("Please enter the first string: ")
    # Get the second string
    str2=input("Please enter the second string: ")
    # Checks if the 2 strings are equal
    if(str1==str2):
        # Prints that they are identical
        print("These 2 strings are identical.")
    # They are not the same
    else:
        # Print that they are not identical
        print("These 2 strings are not identical.")

# The function for option 5
def option_5():
    # Gets the string from the user
    str=input("Please enter a string: ")
    # Enter error loop
    while True:
        # Get the character the user wants to find
        char=input("Please enter a character you want to search: ")
        # Checks if the input is actully 1 character
        if len(char)==1:
            # Break out of error loop if valid
            break
        # No valid
        else:
            # Prints error message
            print("Error: Please enter a valid character")
            # Add an extra line for styling
            print()
    # Makes a empty list for the positions
    pos=[]
    # Makes the string uppercase so they dont clash
    str=str.upper()
    # Makes the character uppercase so they dont clash
    char=char.upper()
    # Go through every letter of the string
    for i in range(len(str)):
        # Check if the letter is the same as the character
        if(str[i]==char):
            # Put the index into the the list
            pos.append(i)
    # Adds an extra line for styling
    print()
    # See how many matches there was
    match len(pos):
        # No matches
        case 0:
            # Print that the letter didnt show up
            print(f"The letter {char} did not appear in the given string.")
        # 1 match
        case 1:
            # Print the one index
            print(f"The letter {char} appeared on index {pos[0]}.")
        # 2 matches
        case 2:
            # Print the two index
            print(f"The letter {char} appeared on index {pos[0]} and {pos[1]}.")
        # 3 or more matches
        case _:
            # Print the begining of the sentence
            print(f"The letter {char} appeared on index ", end="")
            # Go through the list of positions
            for i in range(len(pos)):
                # Print the position
                print(pos[i], end="")
                # Check if its the second last one
                if(i==len(pos)-2):
                    # Print the and part
                    print(", and ", end="")
                # Check if its the last one
                elif(i==len(pos)-1):
                    # Print the dot to end it
                    print(".")
                # Its in the middle
                else:
                    # Print a comma after it
                    print(", ", end="")

# The function for option 6
def option_6():
    # Enter error loop
    while True:
        # Get the string from the user
        str=input("Please enter a >=8 character string: ")
        # Check if the string is long enough
        if(len(str)>=8):
            # Print the letters from index 4 to 6
            print(f"The letter from index 4 to 6 is {str[4]}, {str[5]}, and {str[6]}.")
            # Go back to where its called
            return
        # The string is to short
        else:
            # Prints error message
            print("Error: String is too short")
            # Add an extra line for styling
            print()

# The function for option 7
def option_7():
    # Gets the string from the user
    str=input("Please enter a string: ")
    # Replace all the a with x
    str=str.replace("a", "x")
    # Print the new string
    print(f"Resulting string: {str}")

# Print the title and the menu of options
print(dedent("""
    <== Super String Software ==>

    < Menu of Options >
    1) Return the length of the string
    2) Return the string as all capital letters
    3) Return the letter at the 4th index
    4) Return if 2 strings are identical or not
    5) Search the string for a letter from the user
    6) Return the letters from index 4 to 6
    7) Return a string with all the letters 'a' replaced with the letter 'x'
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
    if(1<=choice<=7):
        # Break out of error loop if valid
        break
    # Invalid choice
    else:
        # Error message
        print("Error: Please enter a valid choice")
        # Prints and extra line styling
        print()

# Print and extra line styling
print()

# See which choice the user chose
match choice:
    # User chose option 1
    case 1:
        # Runs the option 1 function
        option_1()
    # User chose option 2
    case 2:
        # Runs the option 2 function
        option_2()
    # User chose option 3
    case 3:
        # Runs the option 3 function
        option_3()
    # User chose option 4
    case 4:
        # Runs the option 4 function
        option_4()
    # User chose option 5
    case 5:
        # Runs the option 5 function
        option_5()
    # User chose option 6
    case 6:
        # Runs the option 6 function
        option_6()
    # User chose option 7
    case 7:
        # Runs the option 7 function
        option_7()
