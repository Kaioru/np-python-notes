# Functions
In large projects, there are usually many repetitive code. Programmers use functions to group such code together to avoid having to have the same blocks of codes in different sections of the program.

For example calculating the area:
```py
# Without Functions
l = 30
b = 40
print(l * b)

l = 21
b = 32
print(l * b)

l = 65
b = 70
print(l * b)
```
```py
def calculate_area(l, b):
  return l * b

print(calculate_area(30, 40))
print(calculate_area(21, 32))
print(calculate_area(65, 70))
```
See how much cleaner the code looks with functions?
