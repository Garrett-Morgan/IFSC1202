Radius = open("06.01 Radius.txt")

x = Radius.readline()
import math

print('{:>15s} {:>15s} {:>15s} {:>15s}'.format("Radius", "Diameter", "Circumference", "Area"))

while x != "":
    x = float(x)
    diameter = x * 2
    circumference = 2 * (math.pi) * x
    area = (math.pi) * x ** 2
    print('{:15.5f} {:15.5f} {:15.5f} {:15.5f}'.format(x, diameter, circumference, area))
    x = Radius.readline()
Radius.close()
