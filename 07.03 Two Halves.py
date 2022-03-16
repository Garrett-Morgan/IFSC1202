x = str(input("Enter a string: "))
count = len(x)
secondhalf = count // 2
firsthalf = count - secondhalf

print(x[secondhalf:] + x[0:firsthalf])