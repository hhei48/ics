"""
The NAC (Nice ASCII Cipher) models the one-time pad using an XOR cipher and an encryption key that satisfies the one-time pad requirement:
- Random (Uses the secrets module, CSPRNG isn't truely random but virtually impossible to predict)
- Single use
- Full text length
- Securely transmitted (by the user)
It mathematically eliminates brute force attacks. It is called ASCII Nice because the encrypted text and encryption key is printable in one continous line (by replacing unprintable characters as !{ascii}!).

However, this program is insecure in the real world because:
- There are no integrity protection
- The "!" escape characters leak structural information
- Revealing it on screen is insecure
"""

import string
import secrets
import textwrap

KEY_OFFSET=33 # To reduce the chances of having unprintable encrypted characters
PRINTABLE_MIN=34 # Intentionally exlucde !
PRINTABLE_MAX=126
ESCAPE='!'
KEY_BANK=string.ascii_letters+string.digits+string.punctuation

def nac_encrypt(text, key)->str:
    result=[]
    for i in range(len(text)):
        text_ascii=ord(text[i])
        key_ascii=ord(key[i])-KEY_OFFSET
        cur_result=text_ascii^key_ascii
        # Printable characters
        if PRINTABLE_MIN<=cur_result<=PRINTABLE_MAX:
            result.append(chr(cur_result))
        # Unprintable characters
        else:
            result.append(f"{ESCAPE}{cur_result}{ESCAPE}")
    return "".join(result)

def nac_decrypt(text, key)->str:
    result=[]
    itr=0
    for key_char in key:
        # Unprintable character
        if text[itr]==ESCAPE:
            end=text.find(ESCAPE, itr+1)
            # Extract the unprintable character's number
            cur_result=int(text[itr+1:end])
            itr=end
        # Printable character
        else:
            cur_result=ord(text[itr])
        # XOR again to get the original
        cur_result^=ord(key_char)-KEY_OFFSET
        result.append(chr(cur_result))
        itr+=1
    return "".join(result)

# Generate a "random" key
def generate_key(n)->str:
    key=[]
    for _ in range(n):
        # This uses CSPRNG, which is not truely random but virtually impossible to predict
        key.append(KEY_BANK[secrets.randbelow(len(KEY_BANK))])
    return "".join(key)

# Menu and title
print(textwrap.dedent("""
<== NAC ==>
The NAC (Nice ASCII Cipher) is a one-time pad style cipher that generates texts and keys in one continous printable line

< Menu of Options >
1) Encrypt a text
2) Decrypt a text
"""))

# Input choice
while True:
    try:
        choice=int(input("Please select an option: "))
    except ValueError:
        print("Error: Please enter an integer\n")
        continue
    # Choice validation
    if 1<=choice<=2:
        break
    else:
        print("Error: Please enter a valid choice\n")
print()

match choice:
    case 1:
        # Input
        print("Please enter the text you would like encrypt")
        user_text=input("> ")
        # Encryption
        key=generate_key(len(user_text))
        encrypted_text=nac_encrypt(user_text, key)
        # Output
        print(textwrap.dedent(f"""
            ┌─────── Encrypted Text ───────
            │ {encrypted_text}
            └──────────────────────────────
            ┌─────── Encryption Key ───────
            │ {key}
            └──────────────────────────────
        """))
    case 2:
        # Input
        print("Please enter the text you would like to decrypt")
        encrypted_text=input("> ")
        print("Please enter the encryption key")
        key=input("> ")
        # Decryption
        decrypted_text=nac_decrypt(encrypted_text, key)
        # Output
        print(textwrap.dedent(f"""
            ┌─────── Decrypted Text ───────
            │ {decrypted_text}
            └──────────────────────────────
        """))

# This assignment is very fun and very interesting to do!