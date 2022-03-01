def percentchange(x,n):
    return ((x-n) / n) * 100 

n = 0

stock = open("06.02 Stock.txt")

print('{:>10s} {:>10s}'.format("Price", "Change"))

x = stock.readline()

while x != "":
    x = float(x)
    if n == 0:
        print('{:10.2f} '.format(x))
        n = x
        x = stock.readline()
    else:
        percent = (percentchange(x, n))
        n = x
        print('{:10.2f} {:10.2f}'.format(x, percent))
        x = stock.readline()