x = str(input("Enter a string: "))
first = x.find("f") + 1
last = x.find("f", first) + 1

if last != 0:
    print("{}".format(first) + " " + "{}".format(last))
else: print("{}".format(first))