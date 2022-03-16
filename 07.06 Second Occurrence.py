x = str(input("Enter a string: "))
first = x.find("f") + 1
last = x.find("f", first) + 1

if last != 0:
    print("{}".format(last))
if first == 0:
    print("Zero f")
if first != 0 and last == 0:
    print("One f")

