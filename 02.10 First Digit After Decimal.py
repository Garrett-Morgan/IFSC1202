x = float(input("Enter a Number: "))
fraction = x % 1
number = round(fraction,10)
tenth = number // 0.1
truetenth = int(tenth)
print("Tenths Value: " + "{}".format(truetenth))