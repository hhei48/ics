# Stage 1
while True:
    # Inputs the user's string
    print("Stage 1: Please enter a string that is >6 characters.")
    string=input("> ")
    # Check if the string is longer than 6 characters
    if(len(string)>6):
        break
    else:
        print("Error: String must be >6 characters\n")
# Outputs the congratulations message
print("Congratulations! You passed stage 1.\n")

# Stage 2
while True:
    # Inputs the user's string
    print("Stage 2: Please enter a string that contains 'a'.")
    string=input("> ")
    # Check if the string contains 'a'
    if('a' in string):
        break
    else:
        print("Error: String must contain 'a'\n")
# Outputs the congratulations message
print("Congratulations! You passed stage 2.\n")

# Stage 3
while True:
    # Inputs the user's string
    print("Stage 3: Please enter a string that does not contain 'z' and between 5 and 15 characters long.")
    string=input("> ")
    # Check if z is in the string
    if('z' in string):
        print("Error: String must not contain 'z'\n")
        continue
    # Check if the string is between 5 and 15 characters long
    if(5<=len(string)<=15):
        break
    else:
        print("Error: String must be between 5 and 15 characters long\n")
# Outputs the congratulations message
print("Congratulations! You passed stage 3.\n")

# Stage 4
while True:
    # Inputs the user's integer
    print("Stage 4: Please enter an integer between 5 and 500.")
    # Check if the input is an integer
    try:
        num=int(input("> "))
    except ValueError:
        print("Error: Number must be an integer\n")
        continue
    # Check if the integer is between 5 and 500
    if(5<=num<=500):
        break
    else:
        print("Error: Integer must be between 5 and 500\n")
# Outputs the congratulations message
print("Congratulations! You passed stage 4.\n")

# Stage 5
while True:
    # Inputs the user's integer
    print("Stage 5: Please enter a negative integer.")
    # Check if the input is an integer
    try:
        num=int(input("> "))
    except ValueError:
        print("Error: Number must be an integer\n")
        continue
    # Check if the integer is negative
    if(num<0):
        break
    else:
        print("Error: Number must be negative\n")
# Outputs the congratulations message
print("Congratulations! You passed stage 5.\n")

# Stage 6
while True:
    # Inputs the user's integer
    print("Stage 6: Please enter a positive odd integer.")
    # Check if the input is an integer
    try:
        num=int(input("> "))
    except ValueError:
        print("Error: Number must be an integer\n")
        continue
    # Check if the integer is negative
    if not (num>0):
        print("Error: Number must be positive\n")
        continue
    # Check if the integer is odd
    if(num%2):
        break
    else:
        print("Error: Number must be an odd number\n")
# Outputs the congratulations message
print("Congratulations! You passed stage 6.\n")