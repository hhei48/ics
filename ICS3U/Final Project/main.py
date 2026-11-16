import data
import random
import textwrap

def main():
    word=random.choice(data.animals)
    user_word=["_"]*len(word)
    used_letters=[]
    missed_letters=[]

    print(textwrap.dedent("""\
        <== Hangman ==>
        The words in this hangman are all animals.
    """))
    print(data.image[0])

    while "_" in user_word:
        # Print
        print(" ".join(user_word))
        print()

        while True:
            # Input
            print("Guess a letter!")
            guess=input("> ")
            # Invalid guess
            if not guess.isalpha() or len(guess)!=1:
                print("Error: Please enter a valid letter\n")
                continue
            # Used guess
            guess=guess.upper()
            if guess in used_letters:
                print(f"Error: You already used '{guess}'\n")
            else:
                break

        # Wrong guess
        if guess not in word:
            print(f"\nYou've guessed the letter {guess} wrong!")
            missed_letters.append(guess)
            # Print hangman photo
            print(data.image[len(missed_letters)])
        # Right guess
        else:
            print(f"\nYou've guessed the letter {guess} right!")
            for i, char in enumerate(word):
                if guess==char:
                    user_word[i]=guess
        used_letters.append(guess)
        print("──────────────────────────────────────────────────────\n")

        # Win
        if "_" not in user_word:
            print(f"You won! You guessed the word {word}.")
            return

        # Lost
        if len(missed_letters)>=6:
            print(f"You lost! The word is {word}.")
            return

        # Print the stats
        print(f"Missed letters: {" ".join(missed_letters)}")
        print(f"Used letters: {" ".join(used_letters)}")

if __name__ == "__main__":
    main()