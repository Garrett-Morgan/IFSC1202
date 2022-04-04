# Create the array
a = []
# Open the file and read the first line`
citytemps = open("09.06 CityTemps.txt")
x = citytemps.readline()

sum = 0

print("{:8}{:8}{:8}{:8}{:8}{:8}{:8}{:8}{:8}".format("City", "Mo", "Tu", "We", "Th", "Fr", "Sa", "Su", "Avg"))

# While not at end of file
while x != "":

	y = x.split(" ")

	a.append(y)

	x = citytemps.readline()

for i in range(len(a)):
    for j in range(1,len(a[i])):

        num = int(a[i][j])
        sum += num

    avg = sum // len(a[i])
    avg = str(avg)
    sum = 0

    for j in range(1):
        a.append(avg)



for i in range(len(a)):
    for j in range(len(a[i])):

        print("{:7}".format(a[i][j]), end=' ')
    print()
