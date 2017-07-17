number = int(input('Please enter the binary number: '))
valid = True

for c in str(number):
    if not(c == '1' or c == '0'):
        valid = False
        break

print('The binary number is', ['invalid', 'valid'][valid])
