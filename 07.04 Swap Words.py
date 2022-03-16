x = str(input("Enter a string: "))
space = x.find(" ")
secondword = space + 1

print((x[secondword:]) + " " + (x[0:space]))