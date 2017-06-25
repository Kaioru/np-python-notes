string = input('Please enter your program in a string: ')
pendingClosure = 0

i = 0
while i < len(string):
    c = string[i]

    if c == '(':
        pendingClosure += 1
    elif c == ')':
        pendingClosure -= 1

    if pendingClosure < 0:
        break

    i += 1

if pendingClosure == 0:
    print('The program has balanced delimiters.')
else:
    print('The program does not have balanced delimiters.')
