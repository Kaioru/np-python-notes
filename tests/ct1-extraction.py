myList1 = ['ans', 'wer', 'is', 'of']
myList2 = ['-', '+', '*', '/']
myList3 = ['5', 10, 42, '0', '2']

firstDigit = int(myList3[0])
secondDigit = int(str(myList3[2])[0])

print("{}{} {} {} {} {} {} {}".format(
    myList1[0].capitalize(),
    myList1[1],
    myList1[3],
    firstDigit,
    myList2[1],
    secondDigit,
    myList1[2],
    firstDigit + secondDigit))
