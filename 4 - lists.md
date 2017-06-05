# Lists
Data can be sequenced in a list. An example are strings, as strings are a sequence of characters.
```py
listOfNumbers = [1, 2, 3, 4, 5]

print(listOfNumbers[3]) # 4
print(listOfNumbers[-1]) # 5

print(listOfNumbers[0:3]) # [1, 2, 3]
print(listOfNumbers[:3]) # [1, 2, 3]
print(listOfNumbers[2:]) # [3, 4, 5]
```
Notice extraction of data is similar for both strings and lists.

## Operators
```py
listOfFloat = [3.142, 42.42]

print(3.142 in listOfFloat) # True
print(42.42 not in listOfFloat) # False
```

## Functions
```py
listOfNumbers = [1, 2, 3]
listOfString = ['h', 'i']

print(len(listOfNumbers)) # 3
print(min(listOfNumbers)) # 1
print(max(listOfNumbers)) # 3

print(listOfNumbers.append(4)) # [1, 2, 3, 4]
print(listOfString.extend(listOfNumbers)) # ['h', 'i', 1, 2, 3, 4]
```
