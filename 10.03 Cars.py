# Step 1 - Define the class object "Ball"
class Car ():
	
# Step 2 - Define the initializer and any default values

    def __init__(self, Year=0, Make="", Speed=0):

# Step 3 - Define the object attributes

        self.Year = Year
        self.Make = Make
        self.Speed = Speed

# Step 4 - Here is another action
    def Accelerate(self, x): 
        self.Speed =  self.Speed + x
        return self.Speed

    def Brake(self, x): 
        self.Speed =  self.Speed + x
        return self.Speed



# Step 4 - Define Actions (Methods) associated with the object
a = []

cars = open("10.03 Cars.txt", "r")

x = cars.readline()

while x != "":
    y = x.split(",")
    a.append(y)
    x = cars.readline()


for i in range(1):
    for j in range(len(a)):
        car = Car ()

        car.Year = int(a[i][0])
        car.Make = str(a[i][1])

print("Make: {}Year: {}".format(car.Make,car.Year))

print("{:<10s} {:<10s}".format("Change","Speed"))

for i in range(1,len(a)):
    for j in range(1):
        
        x = float(a[i][j])
        
        if x > 0:
            print("{:<10s} {:10.0f}".format(a[i][j],car.Accelerate(x)))

        if x < 0:
            print("{:<10s} {:10.0f}".format(a[i][j],car.Brake(x)))

