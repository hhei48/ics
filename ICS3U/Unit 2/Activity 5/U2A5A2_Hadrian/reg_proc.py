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
        if(len(num)<2):
            print("Error: Please enter at least 2 rational numbers\n")
            continue
        try:
            for i, item in enumerate(num):
                num[i]=float(item)
            break
        except ValueError:
            print("Error: Please enter a valid rational number\n")
            continue
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
    return result
