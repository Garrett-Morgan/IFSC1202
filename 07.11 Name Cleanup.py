def Propercase(x):
    x = x.lower()
    x = x.title()
    return(x)

def RemoveNewLines(x):
    newline = x.find("/n")
    return(x[0:newline])

def Trim(x):
    x = x.strip()
    x = x.rstrip()
    return(x)

def FirstName(x):
    firstspace = x.find(" ")
    return(x[0:firstspace])

def LastName(x):
    lastspace = x.rfind(" ") + 1
    return(x[lastspace:])

def MiddleName(x):
    firstspace = x.find(" ")
    lastspace = x.rfind(" ") + 1
    return(x[firstspace:lastspace])

print('{:10s} {:10s} {:10s}'.format("First", "Middle", "Last"))
print('{:10s} {:10s} {:10s}'.format("----------", "----------", "----------"))



input = open("07.11 Names.txt", "r")

x = input.readline()

while x != "":
    x = str(x)

    output = Propercase(x)

    output = RemoveNewLines(output)

    output = Trim(output)
    
    firstname = str(FirstName(output))

    lastname = str(LastName(output))

    middlename = MiddleName(output)

    middlename = str(Trim(middlename))

    print("{:10s} {:10s} {:10s}".format(firstname,middlename,lastname))
    


    x = input.readline()

