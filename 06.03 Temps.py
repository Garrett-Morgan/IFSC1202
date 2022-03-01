def FahrToCel(x):
    return (x-32)*(5/9)

count = 0

farenheit = open("06.03 FTemps.txt", 'r')

celsius = open("06.03 CTemps.txt", 'w')

x = farenheit.readline()

while x != "":
    count = count + 1

    x = float(x)
    output = FahrToCel(x)

    output = round(output, 1)
    
    output = str(output)
    
    celsius.write(output + "\n")
    x = farenheit.readline()

print( "{}".format(count) + " Records Written.")
celsius.close()
farenheit.close()