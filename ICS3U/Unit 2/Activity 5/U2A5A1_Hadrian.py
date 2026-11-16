import math
import textwrap

def find_mean(num):
    """
    Finds the mean of a rational number set.

    Args:
        num (list[float]): The user's rational number set.

    Returns:
        float: The mean of the num.
    """
    mean=sum(num)/len(num)
    return mean

def find_nth_quartile(num, n):
    """
    Find the n-th quartile of a rational number set.

    Args:
        num (list[float]): The user's rational number set.
        n (int): The n in the n-th quartile

    Return:
        float: The n-th quartile number
    """
    # For simplifying the code below
    m0=len(num)
    m1=m0//2
    m2=m1//2

    # Return the 6 possible cases for the n-th quartile
    match n:
        case 1:
            if(m1%2):
                return num[m2]
            else:
                return (num[m2]+num[m2-1])/2
        case 2:
            if(m0%2):
                return num[m1]
            else:
                return (num[m1]+num[m1-1])/2
        case 3:
            if(m1%2):
                return num[m0-1-m2]
            else:
                return (num[m0-1-m2]+num[m0-m2])/2

def find_sd(num, is_population):
    """
    Finds the population/sample standard deviation of a rational number set.

    Args:
        num (list[float]): The user's rational number set.
        is_population (bool): If the user is finding the population standard deviation or not

    Return:
        float: The population/sample standard deviation of num.
    """
    mean=find_mean(num)
    # Find the standard deviation
    sd=0.0
    for i in num:
        sd+=(i-mean)**2
    # Population SD or Sample SD
    if(is_population):
        sd/=len(num)
    else:
        sd/=len(num)-1
    sd=math.sqrt(sd)
    return sd

def get_set():
    """
    Get and validate a rational number set from user

    Args:
        None

    Returns:
        list: The user's rational number set
    """
    while True:
        print("Please enter a set of rational numbers separated by a space.")
        num_str=input("> ")
        num=num_str.split()

        try:
            for i, item in enumerate(num):
                num[i]=float(item)
            break
        except ValueError:
            print("Error: Please enter a valid rational number\n")
            continue
    print()
    num.sort()
    return num

def get_value_range(input_msg, error_msg, min_range, max_range):
    """
    Get a integer input from the user, and validate the result using a range

    Args:
        input_msg (str): The input message
        error_msg (str): The error message
        min_range (int): Minimum valid value
        max_range (int): Maximum valid value

    Returns:
        int: The validated integer from the user
    """
    while True:
        # Integer input
        try:
            result=int(input(f"{input_msg}: "))
        except ValueError:
            print(f"Error: {error_msg}\n")
            continue
        # Validate range
        if(min_range<=result<=max_range):
            break
        else:
            print(f"Error: {error_msg}\n")
    print()
    return result

print(textwrap.dedent("""
    <== Set Calculator ==>

    < Menu of Options >
    1) Find the mean of a set
    2) Find the median of a p
    3) Find the n-th quartile of a set
    4) Find the population standard deviation of a set
    5) Find the sample standard deviation of a set
    10) Exit
"""))

# Input the menu choice and also the rational number set
choice=get_value_range(
    input_msg="Please enter your choice",
    error_msg="Choice is invalid",
    min_range=1,
    max_range=5
)
num=get_set()

# Menu of options
match choice:
    case 1:
        mean=find_mean(num)
        print(f"The mean is {mean:.1f}.")
    case 2:
        median=find_nth_quartile(num, 2)
        print(f"The median is {median:.1f}.")
    case 3:
        n=get_value_range(
            input_msg="Please enter the quartile number",
            error_msg="Invalid quartile number",
            min_range=1,
            max_range=3
        )
        nth_quartile=find_nth_quartile(num, n)
        print(f"The value of Q{n} is {nth_quartile:.1f}.")
    case 4:
        population_sd=find_sd(num, True)
        print(f"The population standard deviation is {population_sd:.1f}.")
    case 5:
        sample_sd=find_sd(num, False)
        print(f"The sample standard deviation is {sample_sd:.1f}.")
