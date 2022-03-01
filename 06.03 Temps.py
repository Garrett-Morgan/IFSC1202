def FahrToCel(x):
    return (x-32)*(5/9)

farenheit = open("06.03 FTemps.txt", 'r')

celsius = open("06.03 CTemps.txt", 'w')

x = farenheit.readline()

while x != "":
    x = float(x)
    output = FahrToCel(x)

    output = round(output, 1)
    
    output = str(output)
    
    celsius.write(output + "\n")
    x = farenheit.readline()

print("Done.")
celsius.close()
farenheit.close()