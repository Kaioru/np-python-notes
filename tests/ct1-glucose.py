glucoseList = []
previous = False

i = 0
while i < 2:
    glucoseLevel = float(input('Enter glucose level between 0.0 to 50.0: '))
    glucoseList.append(glucoseLevel)
    readings = len(glucoseList)
    average = sum(glucoseList) / readings
    print('Running average of %s reading = %.2f' % (readings, average))

    if (glucoseLevel > 11.10 and not(previous)):
        print('Injecting Insulin now.')
        previous = True
    else:
        print('Already injected in the previous round.')
        previous = False

    i += 1

print('Glucose List =', glucoseList)
