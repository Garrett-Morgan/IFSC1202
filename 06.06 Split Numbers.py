def isEven(x):
    x = int(x)
    even = x % 2 
    if even == 0:
        return True
    else:
        return False

def isOdd(x):
    x = int(x)
    odd = x % 2
    if odd != 0:
        return True
    else:
        return False

def isPrime(x):
    x = int(x)
    for i in range(2, x // 2 + 1):
        result = x / i
        if (result % 1 == 0 ): return False
    else: return True

Oddcount = 0
Evencount = 0
Primecount = 0
Numbercount = 0

input = open("06.06 Numbers.txt", "r")
outputEven = open("06.06 Evennumbers.txt", "w")
outputOdd = open("06.06 Oddnumbers.txt", "w")
outputPrime = open("06.06 Primenumbers.txt", "w")

x = input.readline()

while x != "":
    x = int(x)

    if isEven(x) == True:
        Evencount = Evencount + 1
        x = str(x)
        outputEven.write(x + "\n")

    if isOdd(x) == True:
        Oddcount = Oddcount + 1
        x = str(x)
        outputOdd.write(x + "\n")

    if isPrime(x) == True:
        Primecount = Primecount + 1
        x = str(x)
        outputPrime.write(x + "\n")

    Numbercount = Numbercount + 1

    x = input.readline()
    

print("{}".format(Evencount) + " even numbers.")
print("{}".format(Oddcount) + " odd numbers.")
print("{}".format(Primecount) + " prime numbers.")
print("{}".format(Numbercount) + " numbers.")