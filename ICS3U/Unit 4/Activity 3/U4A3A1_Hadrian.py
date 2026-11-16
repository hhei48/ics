# Declare list
a=[None]*5

# Input
a[0]=int(input("Q1: "))
a[1]=float(input("Q2: "))
a[2]=input("Q3: ")
a[3]=input("Q4: ")
a[4]=input("Q5: ")

# Conversion
a[0]=float(a[0])
a[1]=int(a[1])
a[2]=a[2][0]
a[3]=int(a[3])
a[4]=float(a[4])

# Print empty line for styling
print()

# Output
print(f"1) Whole number integer into a float: {a[0]}")
print(f"2) Decimal number into an integer: {a[1]}")
print(f"3) First character of the name into a char: {a[2]}")
print(f"4) Whole number String into an integer: {a[3]}")
print(f"5) Decimal number String into a float: {a[4]}")