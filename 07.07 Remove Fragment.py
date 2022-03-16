x = str(input("Enter a string: "))

first = x.find("h")
last = x.rfind("h") + 1 

print(x[0:first] + x[last:])