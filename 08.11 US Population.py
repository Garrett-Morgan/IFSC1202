input = open("08.11 USPopulation.txt", "r")

def percentchange(x,n):
    return ((x-n) / n) * 100 

populationlist = []

changelist = []

yearlist = []

percentlist = []

x = input.readline()

year = 1950

lastpopulation = 0

print("{} {:>14} {:>11} {:>18}".format("Year","Population","Change","Percent Change"))      #Heading

while x != "":

    population = int(x) * 1000
    populationlist.append(population)

    percent = percentchange(lastpopulation,population)
    percentlist.append(float(percent))

    change = population - lastpopulation
    changelist.append(int(change))

    lastpopulation = population

    yearlist.append(int(year))
    year += 1

    x = input.readline()

for i in range(len(populationlist)):
    if i != 0:
        print("{} {:14} {:11} {:10.2f}".format(yearlist[i],populationlist[i],changelist[i],percentlist[i]))
    else:
        print("{} {:14} {:>11} {:>10}".format(yearlist[i],populationlist[i],"N/A","N/A"))

minimum = min(changelist)
maximum = max(changelist)
average = (minimum + maximum) // 2

minyear = changelist.index(minimum)
maxyear = changelist.index(maximum)

minyear = yearlist[minyear]
maxyear = yearlist[maxyear]


print("Average change = {}".format(average))
print("Minimum Change = {} ({})".format(minimum,minyear))
print("Maximum Change = {} ({})".format(maximum,maxyear))
