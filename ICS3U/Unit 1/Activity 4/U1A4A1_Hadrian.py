# Output the welcome message
print("<== Welcome to the grade calculator! ==>")

# Line break
print()

# Section title for getting the user's basic information
print("[Basic information]")

# Name input loop
while True:
    # Input the user's name
    name=input("What is your name? ")
    # Checks if the name only contains English letters
    if name.isalpha():
        # Exits the input loop
        break
    else:
        # Tells the user if their input is invalid
        print("Please enter your name in English. ")

# Grade input loop
while True:
    # Input the user's grade as a string
    grade=input("What grade are you in? ")
    # Checks if the grade is an integer AND it is within the valid K-12 range
    if grade.isdigit() and 1<=int(grade)<=12:
        # Casts the string grade input to an integer
        grade=int(grade)
        # Exits the input loop
        break
    else:
        # Tells the user if their input is invalid
        print("Please enter a valid grade.")

# Line break
print()

# "Grades" section where the program gets the user's marks
print("[Grades]")

# Subjects input processing
# All the subjects, English needs capital case
subjects=[
    [None, "math"],
    [None, "English"],
    [None, "biology"],
    [None, "computers"]
]
# Iterate through all the possible subjects
for i, (mark, subject) in enumerate(subjects):
    # Starts the specific subject input loop
    while True:
        # Input the specific subject's mark as a string
        mark=input(f"What is your {subject} score? ")
        # Checks if the specific subject mark is a number AND it is within 100%
        if not mark.isalpha() and 0<=float(mark)<=100:
            # Converts the specific subject mark from string to float
            mark=float(mark)
            # Exits the input loop
            break
        else:
            # Output the reason if it is invalid
            print("Please enter a valid score. ")
    # Assign the mark to the corresponding subject
    subjects[i][0]=mark

# Calculate the average mark of all subjects
mark_sum=0
for mark, subject in subjects:
    mark_sum+=mark
average=mark_sum/len(subjects)

# The result rules for the grades
grades_rule=[
    # Format: (Max score threshold, Result text for output)
    [50, "failed."],
    [60, "a D, work harder."],
    [70, "a C, study better."],
    [80, "a B, good work."],
    [90, "an A, great work!"],
    [100.001, "an A+, excellent!"],
]
# Get the grade letter result base on the average mark
def get_grade_letter_result(mark: float):
    # Iterates through the grade rule to check which bracket does the average mark fits in
    for max_score, result in grades_rule:
        # Checks if the mark is strictly under the max score threshold
        if mark<max_score:
            return result
# Calls the function to get the grade letter result
grade_letter_result=get_grade_letter_result(average)

# Line break
print()

# Print the result section title
print("<== Results ==>")

# Prints the user's name
print(f"Hello {name},")
# Prints the user's grade
print(f"You are in Grade {grade}.")

# Line break
print()

# Outputs all the user's marks
print("Your marks are:")
# Iterate through the subjects
for mark, subject in subjects:
    # Output each subject and the corresponding mark
    print(f"{subject.title()}: {round(mark)}%")

# Line break
print()

# Output the user's average, rounded to 1 decimal places
print(f"Your average is {average:.1f}%")
# Output the grade letter and the comment
print(f"You have {grade_letter_result}")
