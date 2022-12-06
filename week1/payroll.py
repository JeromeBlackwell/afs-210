class Employee:
    def __init__(self, employeeId, firstName, lastName, hourlyPayRate):
        self.employeeID = employeeId
        self.firstName = firstName
        self.lastName = lastName
        self.hourlyPayRate = hourlyPayRate
    
    def Pay(self, hoursWorked):  
         if hoursWorked <= 40: 
            return (hoursWorked * self.hourlyPayRate)
         elif hoursWorked >40: 
            return (40 *self.hourlyPayRate + (hoursWorked -40) * 1.5 *self.hourlyPayRate)
           

           
employeeId = int (input("Enter your Employee ID: "))
firstName =  input("Enter your First Name: ")
lastName = input("Enter your Last Name: ")
hourlyPayRate = float(input("Enter your Hourly Pay Rate: "))
hoursWorked = float(input("Enter total hours worked for the week: "))

newEmployee = Employee(firstName, lastName, employeeId, hourlyPayRate)
print (f'{firstName} {lastName} paycheck amount is {newEmployee.Pay(hoursWorked):.2f}')

