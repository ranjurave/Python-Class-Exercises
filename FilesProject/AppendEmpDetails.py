empOutFile = open('EmpDetails.txt', 'a')
moreToAdd = 'y'
while(moreToAdd == 'y'):
    print('Enter details of employee ')
    empId = input('Enter Employee id ')
    empName = input('Enter employee name ')
    empSalary = input('Enter hourly pay ')
    dept = input('Enter Department ')
    empOutFile.write(empId+'\n')
    empOutFile.write(empName+'\n')
    empOutFile.write(empSalary+'\n')
    empOutFile.write(dept+'\n')
    moreToAdd = input('Do you want to add more employee (y/n)? ')
empOutFile.close()
print('Data entered into the file')