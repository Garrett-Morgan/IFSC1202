# Step 1 - Define the class object "Ball"
class Sketch ():
# Step 2 - Define the initializer and any default values
    def __init__(self, size = [], xpos = 0, ypos = 0, direction = "U", pen = "U"):
# Step 3 - Define the object attributes
        self.size = size
        self.xpos = xpos
        self.ypos = ypos
        self.direction = direction
        self.pen = pen
# Step 4 - Define Actions (Methods) associated with the object
    def init(self):
        n = int(input("Enter the size of the canvas:"))
        a = []
        for i in range(n):
            a.append([' '] * n)
        self.size = a
        return self.size

    def print(self):
        for i in range(len(self.size)):
            for j in range(len(self.size[i])):
                print(self.size[i][j], end=' ')
            print()

    def penup(self):
        self.pen = "U"

    def pendown(self):
        self.pen = "D"

    def turnleft(self):
        if self.direction == "U":
            self.direction = "L"
        elif self.direction == "L":
            self.direction = "D"
        elif self.direction == "D":
            self.direction = "R"
        else:
            self.direction = "U"
        return self.direction

    def turnright(self):
        if self.direction == "U":
            self.direction = "R"
        elif self.direction == "R":
            self.direction = "D"
        elif self.direction == "D":
            self.direction = "L"
        else:
            self.direction = "U"
        return self.direction

    def move(self):
        return 
       
mysketch1 = Sketch()

instructions = []

cshape = open("Cshape.txt", "r")

x = cshape.readline()

while x != "":
    y = x.split(",")
    y = int(y)

    if y[0] == 1:
        mysketch1.penup()
    
    if y[0] == 2:
        mysketch1.pendown()

    if y[0] == 3:
        mysketch1.turnright()

    if y[0] == 4:
        mysketch1.turnleft()

    if y[0] == 5:
        mysketch1.move()