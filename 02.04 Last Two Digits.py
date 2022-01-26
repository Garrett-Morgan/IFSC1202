x = int(input("Enter a Number: "))
tens = x // 10
truetens = tens % 10
ones = x % 10
print("Last Two Digits: " + "{}".format(truetens) + "{}".format(ones))