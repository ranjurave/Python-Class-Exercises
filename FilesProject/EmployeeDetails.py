numOfEmp = int(input('Enter number of Employees '))
empOutFile = open('EmpDetails.txt', 'w')
for x in range(numOfEmp):
    print('Enter details of employee ', x+1)
    empId = input('Enter Employee id ')
    empName = input('Enter employee name ')
    empSalary = input('Enter hourly pay ')
    dept = input('Enter Department ')
    empOutFile.write(empId+'\n')
    empOutFile.write(empName+'\n')
    empOutFile.write(empSalary+'\n')
    empOutFile.write(dept+'\n')
empOutFile.close()
print('Data entered into the file')