# Cases
# 0 binary
# 1 decimal
# 2 hexadecimal
case=[
    [1, 0],
    [1, 2],
    [2, 1],
    [2, 0],
    [0, 2],
    [0, 1]
]

def verbose(case)->str:
    """
        Converts the case number to the base in english

        Args:
            case (int): The case number

        Returns:
            str: The base in english
    """

    match case:
        case 0:
            return "binary"
        case 1:
            return "decimal"
        case 2:
            return "hexadecimal"

def print_menu():
    """
        Prints the menu of options
    """

    print("< Menu of Options >")
    for i in range(6):
        fr=verbose(case[i][0])
        to=verbose(case[i][1])
        print(f"{i+1}) {fr.title()} to {to.title()}")
    print()

# Lookup table
bank=[
    {
        0: "0",
        1: "1"
    },
    {
    },
    {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
]

# Reverse loopup table
reverse_bank=[
    {
        "0": 0,
        "1": 1
    },
    {
    },
    {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }
]
