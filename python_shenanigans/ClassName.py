#Doing the leg work of setting up the class
class Employee:
    'Common base for all employees'
    empcount = 0

    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
        Employee.empcount += 1
        print("The total number of employees: ", Employee.empcount)


    def displaycount(self):
        print("The total number of employees: ", Employee.empcount)

    def displayemployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)

#Listing an intitalization for adding a new employee to the system
emp1 = Employee("Zara", 2000)
emp1.displayemployee()

#Adding second Employee
emp2 = Employee("Manni", 10000)
emp2.displayemployee()

#Add attributes
emp1.age = 25

hasattr(emp1, 'age') #Returns true if 'age' exists
getattr(emp1, 'age') #Returns value of 'age'
setattr(emp1, 'age', 26) #Sets attribute of 'age' to 26
#delattr(emp1, 'age') #deletes attribute of 'age'
