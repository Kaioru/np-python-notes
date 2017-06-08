nric = input("Enter the IC to be validated: ")

total = 4
total += int(nric[1]) * 2
total += int(nric[2]) * 7
total += int(nric[3]) * 6
total += int(nric[4]) * 5
total += int(nric[5]) * 4
total += int(nric[6]) * 3
total += int(nric[7]) * 2

remainder = total % 11
lookup = ['J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
valid = nric[8] == lookup[remainder]

print("Validity of the IC: %s." % valid)
