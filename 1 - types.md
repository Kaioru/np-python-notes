# Types
Data can be classified under different types as such:
- `int` - Integer; number without decimals.
- `float` - Float; number with decimals.
- `bool` - Boolean; true or false value.
- `str` - String; sequence of characters. (e.g text)

```py
type(42) # int - Integer
type(3.142) # float - Float
type(True) # bool - Boolean
type('Hello world!') # str - String
type('42') # str - String;
```
Note the difference in types when there are quotations and when there isn't

## Converting Types
```py
int(3.142)
float(10)
bool('x')
str(10)
```
As long as there is data when using `bool()`, it will always output as `True`.
