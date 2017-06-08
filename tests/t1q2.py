dieselCpl = 2.6391
petrolCpl = 2.3035

litres = float(input("Input the volume of fuel (in litres): "))
dieselCarbon = litres * dieselCpl
petrolCarbon = litres * petrolCpl

print("The carbon dioxide produced by disel is %.2f." % dieselCarbon)
print("The carbon dioxide produced by petrol is %.2f." % petrolCarbon)
