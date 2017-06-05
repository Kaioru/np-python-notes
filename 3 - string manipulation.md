# String Manipulation
A String is a sequence of characters. There are many cases where you wish to extract partial data from a string.
```py
text = 'Hello World'

print(text[4]) # 'o'
print(text[-1]) # 'd'

print(text[0:5]) # 'Hello'
print(text[:4]) # 'Hell'
print(text[6:]) # 'World'
```

## Operators
```py
text = 'Ngee Ann'

print('N' in text) # True
print('A' not in text) # False
```

## Functions
```py
name = 'Adi Septian'

print(len(name)) # 3
print(name.capitalize()) # 'Adi septian'
print(name.upper()) # 'ADI SEPTIAN'
print(name.lower()) # 'adi septian'
print(name.find('s')) # -1
print(name.find('S')) # 4
print(name.replace('Septian', 'Sucks')) # 'Adi Sucks'
```
