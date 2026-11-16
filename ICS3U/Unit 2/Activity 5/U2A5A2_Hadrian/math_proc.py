import math

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
    num.sort()
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

def sort_set(num):
    num.sort()
    for i, item in enumerate(num):
        num[i]=f"{item:g}"
    num=f"S = {{{", ".join(num)}}}"
    return num

def find_var(num, is_population):
    sd=find_sd(num, is_population)
    variance=sd**2
    return variance
