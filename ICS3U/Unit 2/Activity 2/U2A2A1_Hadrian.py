# Print the program title
print("<== Counting Program ==>")
# Print an extra line for styling
print()

# The array that holds all the counting information
count=[
    [0, 10, 1],
    [100, 0, -10],
    [50, 500, 50],
    [6000, 1000, -1000]
]

# Prints the prompt for the user
print("Please enter your choice: ")
# Loop through the counter
for i in range(len(count)):
    # Print each counter choice, the last one need abs for human readability
    print(f"{i+1}... Count from {count[i][0]} to {count[i][1]} by {abs(count[i][2])}")
# Print an extra line for styling
print()

# Enter the error loop
while True:
    # Get the integer choice from the user and subtract by 1 to match the array index
    choice=int(input("Please enter your choice: "))-1
    # Check if the choice is within the array range
    if 0<=choice<=len(count):
        # Breaks out for the error loop if the input the valid
        break
    # Invalid input case
    else:
        # Tells the user the input is wrong
        print("Error: Please enter a valid choice")
        # Print an extra line for styling
        print()

# Print an extra line for styling
print()
# Print a seperator for styling
print("_____________________________________________")
# Print the choice that the user have selected
print(f"You have chosen to count from {count[choice][0]} to {count[choice][1]} by {abs(count[choice][2])}: ")
# Loop through the choice that the user selected
for i in range(count[choice][0], count[choice][1], count[choice][2]):
    # Print i
    print(i)
# Since sometimes you need count[choice][1]-1 or +1, just print the last one here
print(count[choice][1])
# Print a seperator for styling
print("_____________________________________________")
