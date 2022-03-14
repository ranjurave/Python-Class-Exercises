EmployeeDict = {}
empId = 0
AddEmployee = True
while(AddEmployee):
    empId += 1
    EmployeeDict["empId"] = empId
    empName = input("Enter Employee Name: ")
    EmployeeDict["empName"] = empName
    empDept = input("Enter Department Name: ")
    EmployeeDict["empDept"] = empDept
    empCont = bool(input("Is On Contract? y/n : "))
    EmployeeDict["empCont"] = empCont
    AddEmployee = False

for x in EmployeeDict:
    print (x, EmployeeDict[x])

