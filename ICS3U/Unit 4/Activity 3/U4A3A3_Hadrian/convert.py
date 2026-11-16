import bank

def dec_to_result(dec: str, mode)->str:
    """
        Converts decimal number to hexadecimal or binary

        Args:
            dec (int): The user's decimal number
            mode (int): The mode, which is the index of the loopkup table

        Returns:
            str: The converted number
    """
    # Decimal: No conversion needed
    if mode==1:
        return dec

    # Declare
    dec=int(dec)
    result=""
    base=len(bank.bank[mode])

    while dec>0:
        # Use loopup table
        result+=bank.bank[mode][dec%base]
        dec//=base
    # Edge case
    if result=="":
        result="0"
    return result[::-1]

def result_to_dec(result: str, mode)->str:
    """
        Converts hexadecimal or binary number to decimal

        Args:
            result (int): The hexadecimal or binary number
            mode (int): The mode, which is the index of the loopkup table

        Returns:
            str: The decimal number
    """
    # Decimal: No conversion needed
    if mode==1:
        return result

    # Declare
    result=result[::-1]
    dec=0
    base=len(bank.bank[mode])

    # Loop through the number
    for i in range(len(result)):
        # Loop through the reverse loopup table to mnatch
        for j in bank.reverse_bank[mode]:
            if j==result[i]:
                # Use reverse lookup table
                looked_up=bank.reverse_bank[mode][result[i]]
                dec+=looked_up*(base**i)
    return str(dec)
