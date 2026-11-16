# Import the random library
import random

# Store 8 positive and inspiring quotes
quotes = [
    '"Life is like riding a bicycle. To keep your balance, you must keep moving." - Albert Einstein',
    '"The best way to get started is to quit talking and begin doing." - Walt Disney',
    '"You get what you give." - Jennifer Lopez',
    '"We will fail when we fail to try." - Rosa Parks',
    '"You miss 100% of the shots you don\'t take." - Wayne Gretzky',
    '"Always be a first version of yourself and not a second rate version of someone else." - Judy Garland',
    '"A year from now you may wish you had started today." - Karen Lamb',
    '"Slow is smooth and smooth is fast." - Navy SEALs',
]
# Get a random integer in the range of 0 to 7, which corresponds to the quotes array
random_index = random.randrange(0, 7)
# Output a random quote based on the generated random integer
print(quotes[random_index])
