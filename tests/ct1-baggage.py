weight = float(input('Total weight of baggage (kg): '))

if weight > 30:
    additional = weight - 30
    charge = 12 * additional
    print('Your baggage is %.2fkg more than the limit of 30kg.' % additional)
    print('You will have to pay $%.2f' % charge)
else:
    print('You do not have to pay for your baggage.')
