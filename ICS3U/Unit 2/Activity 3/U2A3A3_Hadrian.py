marks = [34.7, 54.1, 34.8, 99.6, 43.6, 43.2, 65.8, 44.8, 88.6]
total = 0
average = 0

print("These are the marks:")

for i in range(9):
    print(marks[i])

for i in range(9):
    total = total + marks[i]
average = total / 9

average = round(average,1)

print("The average mark is:")
print(average)
