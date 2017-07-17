import random

hiddenNum = random.randint(100,999)
cHidden = str(hiddenNum)

print('Mastermind Numbers')
print('')

for attempt in range(0, 10):
    header = 'Try #{} - '.format(attempt + 1)
    guess = int(input('{}Please enter your guess: '.format(header)))

    if guess == hiddenNum:
        print('Oh yeah! You have gotten the correct number!')
        break

    vPosition = 0
    cGuess = str(guess)
    for i in range(0, len(cHidden)):
        if cHidden[i] == cGuess[i]:
            vPosition += 1

    iPosition = 0
    for c in cGuess:
        if c in cHidden:
            iPosition += 1

    iPosition -= vPosition
    print('{}{} correct digit and position, {} correct digit and wrong position.'
          .format(header, vPosition, iPosition))
