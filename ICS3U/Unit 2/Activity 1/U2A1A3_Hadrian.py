# The ruff formatter and linter was used to comply with the Python styling guide

# Import sys for terminating the program with sys.exit(0)
import sys
# Import dedent for easy string formatting
from textwrap import dedent

# Error printing function
def print_error():
    # Prints the error message
    print("Error: Input is invalid. Please enter again.")
    # Prints a new line after the error for readability
    print()

# Prints the title, background story, and the first decision
print(dedent("""
    <==Puck Adventure==>

    Your name is Hadrian. It's your first time playing for Team Wildcats in the
    local beer league. You've been practicing hockey for half a year and you've
    just hopped over the boards to start your first shift as a right-handed
    defenseman in the neutral zone faceoff circle. BUZZ, clack, the puck drops.
    The battle between Team Wildcats and Team Stars starts. Hayden, your team's
    veteran center, wins the faceoff the the puck goes to Haily, your
    left-handed defenseman, so you skate out. Then Haily sends the puck to you
    because the opponent's right wing, Hanson, is pressuring her. You receive
    the puck but you saw the Stars' left winger Harel ramming right at you.

    You must make a decision right away. What are you going to do?
    A) Deke Harel to the right side
    B) Saucer pass to your left winger Hannah
    C) Deke Harel to the left side
"""))

# Enter the error loop
while True:
    # Get an input that corresponds to the above choices, forces upper case
    temp_in = input("Please select A, B, or C: ").upper()
    # Checks if the
    if temp_in == "A":
        # Prints the result and the next decision
        print(dedent("""
            Deke successful! You are now skating pass Harel with the puck
            still on your blade.

            If you rush to the blue line, then your 3 forwards will have
            to wait for you at the blue line. What should you do?
            A) Pass the puck through your center Hayden's skates
            B) Crossover to the right side and send the puck to your
               center Hayden's forehand
        """))
        # Enter the error loop
        while True:
            # Prints the request for input, force upper case
            temp_in=input("Please select A or B: ").upper()
            if(temp_in=="A"):
                # Prints the result and the next decision
                print(dedent("""
                    Hayden recieves the puck poorly but he got poke checked by the
                    opposing center Hayhi, so the puck starts leaking back to the
                    blue line while they both rush to get the puck. What are you doing?
                    A) Start skating backward to defend Hayhi
                    B) Skate right to get the puck before it exits the blue line
                """))
                # Enter the error loop
                while True:
                    # Prints the request for input, force upper case
                    temp_in=input("Please enter A or B: ").upper()
                    # Check which path it goes
                    if temp_in=="A":
                        # Prints the result
                        print(dedent("""
                            Hayhi gets the puck successfully and sends it right past you to Harel.
                            An odd man rush has started :c as Haily cannot defend Hayhi and intercept
                            passes to Hanson at the same time. Hayhi skates forward, shoots, and scores!
                        """))
                        # Terminate the program
                        sys.exit(0)
                    # Check which path it goes to
                    elif temp_in=="B":
                        # Prints the result
                        print(dedent("""
                            You intercepted the puck again and clap bomb from the blue line.
                            O_O YOU SCORED!!!
                        """))
                        # Terminate the program
                        sys.exit(0)
                    else:
                        # Prints the error message
                        print_error()
            # Check which path it goes
            elif(temp_in=="B"):
                # Prints the result
                print(dedent("""
                    Hayden gets the puck, but the opposing defenseman comes to intercept the
                    shooting. Hayden then fake shot the opposing goalie, sends the puck left to
                    Hannah. The goalie struggles to move left quickly as Hannah shoots and scores!
                """))
                # Terminate the program
                sys.exit(0)
            # Error handling
            else:
                # prints error message
                print_error()
    # Check which path it goes
    elif temp_in == "B":
        # Prints the result
        print(dedent("""
            Hannah, your left winger gets the puck, but she is getting
            pressured by the Stars' right-handed defenseman Hagel, so
            she passed the puck to Hayden in the offensive zone.
            Bang! Team Wildcats scored with a one timer!
        """))
        # Terminate the program
        sys.exit(0)
    # Check which path it goes to
    elif temp_in == "C":
        # Prints the result
        print(dedent("""
            You got poke checked by Harel! He grabbed the puck and started a breakaway :c
            Oh no! You skate back with full force but you can't reach Harel. He tries to shoot
            but slipped and crash into your goalie Ms. O'Halloran, which happens to be your teacher.
            You, Haily, and Hayden skates back to check what is going on.
        """))
        # Enter error loop
        while True:
            # Prints the request for input, force upper case
            temp_in = input("Should we all start a scrum? (Y/N): ").upper()
            # Check which path to go
            if temp_in == "Y":
                # Prints the result
                print("You're not in the NHL! 1 game misconduct, bye!")
                # Terminate the program
                sys.exit(0)
            # Check which path to go
            elif temp_in == "N":
                # Prints the result and the next decision
                print(dedent("""
                    BEEP! The refs stops the play. What you doing next?
                    A) Watch aside as the refs check on them
                    B) Check if Ms. O'Halloran is injured
                """))
                # Enter error loop
                while True:
                    # Prints the request for input, force upper case
                    temp_in = input("Please select A or B: ").upper()
                    # Check which path to go
                    if temp_in == "A":
                        # Prints the result
                        print(
                            "Bad team spirit :/ Back to the bench immediately!"
                        )
                        # Terminate the program
                        sys.exit(0)
                    # Check which path to go
                    elif temp_in == "B":
                        # Prints the result
                        print(dedent("""
                            Good team spirit! Luckily both players are not
                            injured. You three skates back to the faceoff
                            circle to play again.
                        """))
                        # Terminate the program
                        sys.exit(0)
                    # Error handling
                    else:
                        # Prints the error message
                        print_error()
            # Error handling
            else:
                # Prints the error message
                print_error()
    # Error handling
    else:
        # Prints the error message
        print_error()
