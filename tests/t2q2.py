import random

hiddenNum = random.randint(100, 999)

print('Mastermind Numbers')
print('')

for attempt in range(0, 10):
    header = 'Try #{} - '.format(attempt + 1)
    guess = int(input('{}Please enter your guess: '.format(header)))

    if guess == hiddenNum:
        print('Oh yeah! You have gotten the correct number!')
        break
    print('{}Your guess was incorrect.'.format(header))
