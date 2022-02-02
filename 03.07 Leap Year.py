x = int(input("Enter Four Digit Number: "))
notleap = x % 100 == 0
isleap = x % 4 == 0
isleap2 = x % 400 == 0
if(isleap == True):
    if(notleap == False): print("LEAP YEAR")
    elif(isleap2 == True): print("LEAP YEAR")
else: print("COMMON YEAR")