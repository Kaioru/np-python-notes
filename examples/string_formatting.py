name = 'World'

# Basic Formatting
print(f'Hello, {name}!')
print('Hello, %s!' % name)
print('Hello, {}!'.format(name))

# Table Formatting
x1 = 2
x2 = 1

print('{:<14}{:<14}{:<14}'.format('Number', 'Multiplier', 'Answer'))
while x2 <= 10:
    answer = x1 * x2
    print('{:<14}{:<14}{:<14}'.format(x1, x2, answer))
    x2 += 1
