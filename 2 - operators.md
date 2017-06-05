# Operators
Data can be operated on with the use of operators.

## Arithmetic Operators
Used to operator one data with another to generate a new data.
- `+` - Addition
- `-` - Subtraction
- `*` - Multiplication
- `**` - Exponentiation
- `/` - Division
- `//` - Division (Floor)
- `%` - Modulus

```py
print(1 + 1) # 2
print(10 - 2.4) # 7.6
print(5 * 2) # 10
print(2 ** 2) # 4
print(10 / 3) # 3.333..
print(10 / 7) # 1
print(100 % 40) # 20

print('Hello' + ' ' + 'world') # Hello world
print('Nyan' * 3) # NyanNyanNyan
```
Notice the difference when using operators between strings and between integers.

## Rational Operators
Used to compare between two datas and generates a `bool` of the result.
- `==` - Equal
- `!=` - Not equal
- `>` - Greater than
- `>=` - Greater than or equal
- `<` - Less than
- `<=` - Less then or equal
```py
print('Hello' == 'World') # False
print(1 != 2) # True
print(42 > 69) # False
print(20 >= 20) # True
print(100 < 50) # False
print(25 <= 50) # True

print(1 == '1') # False
```
Notice the comparison between an integer and string.
