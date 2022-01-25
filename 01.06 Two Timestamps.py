print("First Timestamp")
x = input("Enter Hours: ")
y = input("Enter Minutes: ")
z = input("Enter Seconds: ")
print("Second Timestamp")
a = input("Enter Hours: ")
b = input("Enter Minutes: ")
c = input("Enter Seconds: ")
x1 = (int(x)*3600)
y1 = (int(y)*60)
z1 = (int(z))
a1 = (int(a)*3600)
b1 = (int(b)*60)
c1 = (int(c))
sum1 = x1 + y1 + z1
sum2 = a1 + b1 + c1
difference = sum2 - sum1
truediff = str(difference)
print(truediff)