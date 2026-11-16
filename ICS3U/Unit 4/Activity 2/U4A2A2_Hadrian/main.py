import textwrap

def factorial(n: int)->int:
    """
        Find factorial using linear multiplication

        Args:
            n (int): The n in n!

        Returns:
            int: The value of n!
    """
    num=1
    for i in range(2, n+1):
        num*=i
    return num

def is_prime(n: int)->str:
    """
        Determine if n is a prime through repeated division

        Args:
            n (int): The number that needed to be tested

        Returns:
            str: True or False in the compatible sentence format
    """
    if n==1:
        return "not "
    # I did +1 for all cases
    for i in range(2, n//2+1):
        if n%i==0:
            return "not "
    return ""

def fib(n: int)->int:
    """
        Find the n-th fibonacci number using recursion

        Args:
            n (int): The n in the n-th fibonacci number

        Returns:
            int: The n-th fibonacci number
    """
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

# Title and menu of options
print(textwrap.dedent("""
    <== Factorial, Prime Number, Fibonacci Calculator ==>

    Menu of Options:
    1) Find the factorial of a given integer
    2) Determine if a given integer is a prime number
    3) Find the fibonacci value given an integer index
"""))

# Error loop for menu of options input
while True:
    try:
        choice=int(input("Please select an option: "))
    except ValueError:
        print("Error: Please enter an integer\n")
        continue
    if 1<=choice<=3:
        break
    else:
        print("Error: Please enter a valid option\n")
        continue

# Error loop for the input value
while True:
    try:
        num=int(input(f"Please enter an integer for option {choice}: "))
    except ValueError:
        print("Error: Please enter an integer\n")
    # Positive integer
    if num>0:
        break
    else:
        print("Error: Please enter a positive integer\n")
        continue

print()

# Menu of options output and calling functions
match choice:
    case 1:
        print(f"{num}! is equals to {factorial(num)}.")
    case 2:
        print(f"{num} is {is_prime(num)}a prime number.")
    case 3:
        print(f"The fibonacci number at index {num} is {fib(num)}.")