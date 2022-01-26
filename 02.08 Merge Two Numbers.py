x = int(input("Enter Two Digit Number: "))
y = int(input("Enter Two Digit Number: "))
ones = x % 10
twodigit = x // 10
tens = twodigit % 10
secones = y % 10
sectwodigit = y // 10
sectens = sectwodigit % 10
print("Merged Numbers: " + "{}".format(tens) + "{}".format(sectens) + "{}".format(ones) + "{}".format(secones))
