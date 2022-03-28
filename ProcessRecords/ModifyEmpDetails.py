import os
searchEmpName = input('Enter Employee Name: ')
newPay = float(input('Enter new Pay: '))
empInFile = open('EmpDetails.txt', 'r')
empInFileTemp = open('EmpDetailsTemp.txt', 'w')
foundFile = False
line = empInFile.readline()
while(line!=''):
    empId = int(line)
    empName = empInFile.readline()
    empName = empName.strip('\n')
    empPay = float(empInFile.readline())
    empDept = empInFile.readline()
    empDept = empDept.strip('\n')
    if(empName == searchEmpName):
        empInFileTemp.write(str(empId)+'\n')
        empInFileTemp.write(empName+'\n')
        empInFileTemp.write(str(newPay)+'\n')
        empInFileTemp.write(empDept+'\n')
        foundFile = True
    else:
        empInFileTemp.write(str(empId)+'\n')
        empInFileTemp.write(empName+'\n')
        empInFileTemp.write(str(empPay)+'\n')
        empInFileTemp.write(empDept+'\n')
    line = empInFile.readline()
empInFileTemp.close()
empInFile.close()
os.remove('EmpDetails.txt')
os.rename('EmpDetailsTemp.txt', 'EmpDetails.txt')
if(foundFile):
    print('Details changed')
else:
    print('File not found!')