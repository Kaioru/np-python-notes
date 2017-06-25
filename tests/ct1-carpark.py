import math

entryTime = float(input('Entry time of the vehicle: '))
exitTime = float(input('Exit time of the vehicle: '))

hours = math.ceil(exitTime - entryTime)
perEntry = 0.0

if exitTime >= 18.00:
    if (exitTime - entryTime > 1):
        perEntry = 4.0
    if (entryTime < 18.00):
        hours = math.ceil(18.00 - entryTime)
    else:
        hours = 0
charge = min(7.50, 1.50 * hours + perEntry)

print('The carpark charge is $%.2f' % charge)
