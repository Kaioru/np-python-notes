# Loops
There are many cases a programmer would want to repeat same or similar code blocks for n amount of times.
```py
n = 0
while n < 3:
  print(n)
  n += 1
```
This while-loop code will run 3 times with the variable `n` going from 0 to 2.

```py
for n in range(0, 3)
  print(n)
```
This for-loop code will generate the same output as the previous while-loop code. Notice how much simpler it looks?

## Control Flow
```py
n = 0
while n < 10:
  if n == 3:
    break
  n += 1
```
This while-loop code will continue running until the 4th loop, where it will satisfy the `n == 3` condition which will break the loop, skipping the rest of the loop (4th to 9th).

```py
n = 0
for n in range(0, 5)
  if n == 2:
    continue
  print(n)
```
This for-loop code will run 5 times which the `n` variable will go from 0 to 4. However, on the 3rd loop, where it will satisfy the `n == 2` condition which will trigger the `continue` statement. This statement will skip to the next loop, skipping the `print(n)` statement.
