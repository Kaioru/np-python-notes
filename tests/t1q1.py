v = float(input("Input the take-off speed: "))
a = float(input("Input the acceleration: "))

length = (v ** 2) / (2 * a)

print("The minimum runway length is %f." % length)
