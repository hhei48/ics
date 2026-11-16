numbers = []
total = 0

print("Enter twenty integers and they will be added together:")
for i in range(20):
    numbers.append(int(input()))
for i in range(20):
    total = total + numbers[i]

print("The sum of those numbers is:")
print(total)
