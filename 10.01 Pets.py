# Step 1 - Define the class object "Ball"
class Pet ():
	
# Step 2 - Define the initializer and any default values
	def __init__(self, Name="", Type="", Age=0):

# Step 3 - Define the object attributes
		self.Name = Name
		self.Type = Type
		self.Age = Age

print("{:10s} {:10s} {:10s}".format("Name", "Type", "Age"))

# Step 4 - Define Actions (Methods) associated with the object
a = []

pets = open("10.01 Pets.txt", "r")

x = pets.readline()

while x != "":
    y = x.split(",")
    a.append(y)
    x = pets.readline()

for i in range(len(a)):
    for j in range(1):
        pet = Pet ()
        
        pet.name = str(a[i][0])
        pet.type = str(a[i][1])
        pet.age = int(a[i][2])
        print("{:10s} {:10s} {:<10.0f}".format(pet.name, pet.type, pet.age))        # Print the attributes
