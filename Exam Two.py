a = []
totalsales = 0
totalcars = 0
price = 0
count = 0

carsales = open("CarSales.txt", "r")

x = carsales.readline()

while x != "":
    y = x.split(",")
    a.append(y)
    x = carsales.readline()

for i in range(len(a)):
    for j in range(1,len(a[i])):
        price = int(a[i][j])
        totalsales += price
        totalcars += 1

avgprice = totalsales / totalcars
avgprice = round(avgprice)

print("{} Total Cars. - Average Price {}.".format(totalcars, avgprice))

entry = input(str("Enter Car Make: "))
entry = entry.lower()
entry = entry.title()

if entry == "":
    quit()

else:
    if entry == "Saab":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Saab":
                   price += int(a[i][1])
                   count += 1

    if entry == "Audi":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Audi":
                   price += int(a[i][1])
                   count += 1

    if entry == "Aston Martin":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Aston Martin":
                   price += int(a[i][1])
                   count += 1


    if entry == "Pontiac":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Pontiac":
                   price += int(a[i][1])
                   count += 1


    if entry == "Chevorlet":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Chevorlet":
                   price += int(a[i][1])
                   count += 1

    if entry == "Gmc":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Gmc":
                   price += int(a[i][1])
                   count += 1

    
    if entry == "Mazda":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Mazda":
                   price += int(a[i][1])
                   count += 1

    
    if entry == "Dodge":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Dodge":
                   price += int(a[i][1])
                   count += 1

    
    if entry == "Toyota":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Toyota":
                   price += int(a[i][1])
                   count += 1

    
    if entry == "Bmw":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Bmw":
                   price += int(a[i][1])
                   count += 1

    
    if entry == "Volkswagen":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Volkswagen":
                   price += int(a[i][1])
                   count += 1

    if entry == "Volvo":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Volvo":
                   price += int(a[i][1])
                   count += 1

    if entry == "Subaru":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Subaru":
                   price += int(a[i][1])
                   count += 1

    if entry == "Mercedes Benz":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Mercedes Benz":
                   price += int(a[i][1])
                   count += 1

    if entry == "Oldsmobile":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Oldsmobile":
                   price += int(a[i][1])
                   count += 1

    if entry == "Maybach":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Maybach":
                   price += int(a[i][1])
                   count += 1
    
    if entry == "Buick":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Buick":
                   price += int(a[i][1])
                   count += 1

    if entry == "Rolls Royce":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Rolls Royce":
                   price += int(a[i][1])
                   count += 1

    if entry == "Lexus":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Lexus":
                   price += int(a[i][1])
                   count += 1

    if entry == "Ford":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Ford":
                   price += int(a[i][1])
                   count += 1

    if entry == "Lincoln":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Linconln":
                   price += int(a[i][1])
                   count += 1

    if entry == "Suzuki":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Suzuki":
                   price += int(a[i][1])
                   count += 1

    if entry == "Porshe":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Porshe":
                   price += int(a[i][1])
                   count += 1

    if entry == "Scion":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Scion":
                   price += int(a[i][1])
                   count += 1

    if entry == "Chrysler":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Chrysler":
                   price += int(a[i][1])
                   count += 1

    if entry == "Jaguar":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Jaguar":
                   price += int(a[i][1])
                   count += 1

    if entry == "Jeep":
        for i in range(len(a)):
            for j in range(1,len(a[i])):
                if a[i][0] == "Jeep":
                   price += int(a[i][1])
                   count += 1

    else:
        print("Car Make Not Found.")
        


averageprice = price / count
averageprice = round(averageprice)

averagepercent = (averageprice - avgprice) / avgprice * 100
averagepercent = round(averagepercent)

print("{} Cars Sold".format(count))
print("${} Average Price".format(averageprice))
print("{}% Above/Below Average".format(averagepercent))
