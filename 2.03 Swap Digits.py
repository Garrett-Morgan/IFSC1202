x = int(input("Enter a 2 digit Number: "))
tens = x // 10
ones = x % 10
print("{}".format(ones) + "{}".format(tens))