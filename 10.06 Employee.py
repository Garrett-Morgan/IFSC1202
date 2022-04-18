# Step 1 - Define the class object "Ball"
class Employee ():

# Step 2 - Define the initializer and any default values
    def __init__(self,FirstName="",LastName="",IDNumber=0,HoursWorked=0,Wage=0):

# Step 3 - Define the object attributes
        self.FirstName = FirstName
        self.LastName = LastName
        self.IDNumber = IDNumber
        self.HoursWorked = HoursWorked
        self.Wage = Wage
    
    def WeeklyPay(self):
        weeklypay = self.HoursWorked * self.Wage
        return weeklypay


# Step 4 - Define Actions (Methods) associated with the object
a = []

payroll = open("10.06 Payroll.txt", "r")

x = payroll.readline()

while x != "":
    y = x.split(",")
    a.append(y)
    x = payroll.readline()

for i in range(1):
    for j in range(1):
        employee1 = Employee()
        employee2 = Employee()
        employee3 = Employee()
        
        employee1.FirstName = str(a[0][0])
        employee1.LastName = str(a[0][1])
        employee1.IDNumber = int(a[0][2])
        employee1.HoursWorked = int(a[0][3])
        employee1.Wage = float(a[0][4])

        employee2.FirstName = str(a[1][0])
        employee2.LastName = str(a[1][1])
        employee2.IDNumber = int(a[1][2])
        employee2.HoursWorked = int(a[1][3])
        employee2.Wage = float(a[1][4])

        employee3.FirstName = str(a[2][0])
        employee3.LastName = str(a[2][1])
        employee3.IDNumber = int(a[2][2])
        employee3.HoursWorked = int(a[2][3])
        employee3.Wage = float(a[2][4])


print("{} {} {} {} {} {}".format("First Name","Last Name","ID Number","Hours Worked","Hourly Wage","Weekly Pay"))
print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(employee1.FirstName, employee1.LastName, employee1.IDNumber, employee1.HoursWorked, employee1.Wage, employee1.WeeklyPay()))
print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(employee2.FirstName, employee2.LastName, employee2.IDNumber, employee2.HoursWorked, employee2.Wage, employee2.WeeklyPay()))
print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(employee3.FirstName, employee3.LastName, employee3.IDNumber, employee3.HoursWorked, employee3.Wage, employee3.WeeklyPay()))