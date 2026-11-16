# Print the program title
print("<== The Time Calculator ==>")
# Prints the program's description
print("The time calcualtor converts seconds into days, hours, and minutes.\n")

# Enter the error loop for the second input
while True:
    # Try to input the seconds
    try:
        # Input the second and convert to integer
        second=int(input("Enter the number of seconds: "))
    # Second is not an integer
    except ValueError:
        # Tell the user to input an intger
        print("Error: Please enter an integer.")
        # Go back to the start of the error loop
        continue
    # Check if the second is negative
    if second<0:
        # Tell the user it cannot be negative
        print("Error: Please enter a valid time.")
    # Integer is 0 or positive
    else:
        # Exits the error loop
        break

# Store the origianl second input for output later
original=second

# Integer divide the day in seconds
day=second//86400
# Get the remainder
second%=86400

# Intger divide the hour in seconds
hour=second//1440
# Get the remainder
second%=1440

# Intger divide the minute in seconds
minute=second//60
# Get the remainder
second%=60

# Print the converted time
print(f"\n{original}s is equals to {day}:{hour:02d}:{minute:02d}:{second:02d}")

