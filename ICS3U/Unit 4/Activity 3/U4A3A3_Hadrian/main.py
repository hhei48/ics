import convert
import bank

def main():
    # Print title and menu
    print("<== Decimal Binary Hexadecimal Converter ==>\n")
    bank.print_menu()

    # Get the base numbers from choice
    fr, to=bank.case[get_choice()]

    # Input
    user_num=input(f"Please enter the {bank.verbose(fr)} number: ")
    # Convert input to medium
    user_num=convert.result_to_dec(user_num, fr)
    # Convert medium to output
    result=convert.dec_to_result(user_num, to)
    # Output
    print(f"The {bank.verbose(to)} form is {result}.")

def get_choice():
    """
        Inputs and validates the user's choice
    """

    while True:
        try:
            print("Please choose an option")
            choice=int(input("> "))
            print()
        except ValueError:
            print("Error: Please enter an integer\n")
            continue
        # Validate choice
        if 1<=choice<=6:
            break
        else:
            print("Error: Please enter a valid choice\n")
    # -1 to fit the cases
    return choice-1

if __name__ == "__main__":
    main()