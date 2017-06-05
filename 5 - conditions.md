# Conditions
There are many cases when you want to limit a certain program behavior to a certain condition.
```py
if 1 + 1 == 2:
  print('1 + 1 is indeed 2!')
```

There are also many uses when there are multiple conditions.
```py
life = 42

if 1 + 1 == 2 and life == 42:
  print('1 + 1 is still 2 and life equals 42!')
```

Also multiple conditions with different behaviors.
```py
score = 42

if score <= 50:
  print('You failed the test!')
elif score <= 75:
  print('You got a B!')
else:
  print("You got an A! Congratulations!")
```

## Elvis Operator
Writing if statements for 1 line codes can be ugly and messy at times.
```py
a = 'Pen'
b = 'Pineapple'

print(a if True else b) # 'Pen'
print(a if False else b) # 'Pineapple'
```

## Logical Operators
```py
print(True or False) # True
print(True or True) # True
print(False or False) # False
print(False and False) # False
print(True and False) # False
print(True and True) # True
```
