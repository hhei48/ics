# The MDM4U Essentials Calculator is created because
# there are multiple questions asking you to calculate
# the standard deviation by hand with a set that is
# 15 rational numbers long. It is extremely time consuming.

# Import the square root function for square root
from math import sqrt

# Prints the program title
print("<== MDM4U Essentials Calculator ==>")
# Prints an extra line for styling
print()

# Enter the error loop
while True:
    # For detecting error in the conversion loop
    has_error=False

    # Prompts the user to enter the data set
    print("Please enter a set of rational numbers separated by a space.")
    # Inputs in a separate line because these sets are usually very long
    num_str=input("> ")

    # Separate each value to turn into an array
    num=num_str.split()
    # Convert the input strings into a float
    for i in range(len(num)):
        # Error handling
        try:
            # Try if you can convert each list element to float
            num[i]=float(num[i])
        # Cannot convert
        except ValueError:
            # Flip the error
            has_error=True
            # Print the error statement
            print("Error: Please enter a valid rational number")
            # Print an extra line for styling
            print()
    # Loop again if have error
    if has_error:
        continue
    # Break if there are no error
    else:
        break
# Prints an extra line for styling
print()

# Sort the list of floats
num.sort()

# Prints the sorted set with styling
print("Sorted set = {", end="")
for i in range(len(num)):
    # Prints the i-th sorted number
    print(num[i], end="")
    # Last one does not need a comma
    if(i<len(num)-1):
        # Prints the comma if i is not the last position
        print(", ", end="")
# Wraps the printed set up
print("}")

# Initiate the empty mean
mean=0.0
# Loop through the list
for i in num:
    # Add all the numbers
    mean+=i
# Divide by the number of elements to get the mean
mean/=len(num)
# Print the mean rounded to 2 decimals places
print(f"Mean = {mean:.2f}")

# Initiate the empty standard deviation
sd=0.0
# Loop through the list
for i in num:
    # standard deviation formula
    sd+=(i-mean)**2
# Divide by the number of elements
sd/=len(num)
# Square root the result
sd=sqrt(sd)
# Prints the standard deviation
print(f"SD σ = {sd:.2f}")
