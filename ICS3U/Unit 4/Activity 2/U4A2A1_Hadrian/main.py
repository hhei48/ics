# Use classes to make the array easier to read
class zirboin_coin:
    def __init__(self, value, name, count):
        self.value=value
        self.name=name
        self.count=count

# Setup the coin info array
bank=[
    zirboin_coin(100000, 'drobzit', 0),
    zirboin_coin(50000, 'clickwick', 0),
    zirboin_coin(10000, 'gazoontight', 0),
    zirboin_coin(1000, 'frazoint', 0),
    zirboin_coin(500, 'blointoint', 0),
    zirboin_coin(1, "vrobits", 0)
]

print("<== Zirboin Bank Vrobits Compression Calculator ==>\n")

# Input the user's amount
while True:
    try:
        amount=int(input("Please enter the number of vrobits: "))
        break
    except ValueError:
        print("Error: Please enter an integer\n")

print(f"\nUsing ideal coins, {amount} vrobits equals to:")

# Calculate the amount of coins needed for each coin type
for coin in bank:
    if amount>=coin.value:
        coin.count+=amount//coin.value
        amount%=coin.value

# Only prints coins that is used
for coin in bank:
    if coin.count>0:
        print(f"- {coin.count} {coin.name}")