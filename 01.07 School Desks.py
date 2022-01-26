x = int(input("Enter Classroom A: "))
y = int(input("Enter Classroom B: "))
z = int(input("Enter Classroom C: "))
x1 = x // 2
y1 = y // 2
z1 = z // 2
x2 = x % 2
y2 = y % 2
z2 = z % 2
sum = x1 + y1 + z1 + x2 + y2 + z2
desks = str(sum)
print(desks)
