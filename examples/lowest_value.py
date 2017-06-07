"""Prints the lowest integer value in a list"""

listOfNumbers = [53, 77, 34, 94, 21]
lowestValue = 100

# 1 - While-loop
x = 0
while x < len(listOfNumbers):
    number = listOfNumbers[x]
    if number < lowestValue:
        lowestValue = number
    x += 1

print(lowestValue)

# 2 - For-loop
for number in listOfNumbers:
    if number < lowestValue:
        lowestValue = number

print(lowestValue)

# 3 - 'min' function
print(min(listOfNumbers))
