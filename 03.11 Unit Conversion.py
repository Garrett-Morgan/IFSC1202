FromValue = float( input("Enter from Value: "))

FromUnit = input("Enter from Unit(in, ft, yd, mi): ")
if(FromUnit in("in", "ft", "yd", "mi")):
    print("Nice")
else: print("FromUnit not Valid.") (quit())

ToUnit = input("Enter to Unit(in, ft, yd, mi): ")
if(ToUnit in("in", "ft", "yd", "mi")):
    print("Nice")
else: print("ToUnit not Valid.") (quit())       #End of Inputs

if(FromUnit in("in")):       #if FromValue = in
    if(ToUnit in("in")): print(FromValue)

    if(ToUnit in("ft")): 
        ToValue = (FromValue / 12)
        (print(ToValue))

    if(ToUnit in("yd")): 
        ToValue = (FromValue / 36)
        (print(ToValue))

    if(ToUnit in("mi")): 
        ToValue = (FromValue / 63360)
        (print(ToValue))

if(FromUnit in("ft")):        #if Fromvalue = ft
    if(ToUnit in("in")):
        ToValue = FromValue * 12
        print(ToValue)

    if(ToUnit in("ft")): 
        ToValue = (FromValue)
        (print(ToValue))

    if(ToUnit in("yd")): 
        ToValue = (FromValue / 3)
        (print(ToValue))

    if(ToUnit in("mi")): 
        ToValue = (FromValue / 5280)
        (print(ToValue))

if(FromUnit in("yd")):        #if Fromvalue = yd
    if(ToUnit in("in")):
        ToValue = FromValue * 36
        print(ToValue)

    if(ToUnit in("ft")): 
        ToValue = FromValue * 3
        (print(ToValue))

    if(ToUnit in("yd")): 
        ToValue = (FromValue)
        (print(ToValue))

    if(ToUnit in("mi")): 
        ToValue = (FromValue / 1760)
        (print(ToValue))

if(FromUnit in("mi")):        #if Fromvalue = mi
    if(ToUnit in("in")):
        ToValue = FromValue * 63360
        print(ToValue)

    if(ToUnit in("ft")): 
        ToValue = FromValue * 5280
        (print(ToValue))

    if(ToUnit in("yd")): 
        ToValue = (FromValue * 1760)
        (print(ToValue))

    if(ToUnit in("mi")): 
        ToValue = FromValue
        (print(ToValue))