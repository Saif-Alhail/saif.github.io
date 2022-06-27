class Employee:
    leave_count = 0
    def __init__(self, name, pos, dep, leave):
        self.name = name
        self.position = pos
        self.department = dep
        self.leave = leave
        if self.leave:
            Employee.leave_count = Employee.leave_count + 1
        
    def displayEmployee(self):
        if self.leave:
            print ("Employee Name: ", self.name)
            print ("Employee Position: ", self.position)
            print ("Employee Department: ", self.department)
            print ("Employee Leave Request: ", self.leave)
        else:
            pass
        
first_employee = Employee ("John", "Bookkeeper", "Accounting", ["06 November 2022 to 22 November 2022"])
second_employee = Employee ("Steve", "Project Manager", "Management", ["04 December 2022 to 14 December 2022"])
third_employee = Employee ("Paul", "Developer", "Software Team", [])
fourth_employee = Employee ("Andrew", "Senior - Developer", "Software Team", [])

first_employee.displayEmployee()
second_employee.displayEmployee()
third_employee.displayEmployee()
fourth_employee.displayEmployee()