pay = float(input('Enter Pay Rate : '))
empInFile = open('EmpDetails.txt', 'r')
line = empInFile.readline()
empNum = 0
while(line!=''):
    empId = line
    empId = empId.strip('\n')
    empIdConvert = int(empId)
    empName = empInFile.readline()
    empName = empName.strip('\n')
    empPay = empInFile.readline()
    empPay = empPay.strip('\n')
    empPayConverted = float(empPay)
    empDept = empInFile.readline()
    empDept = empDept.strip('\n')
    empNum += 1
    if(empPayConverted > pay):
        print('Details of Employee ', empNum)
        print('------------------------------')
        print('Emp Id : ', empId)
        print('Employee Name : ',empName )
        print('Employee Pay : ',empPay )
        print('Dept : ',empDept)
    line = empInFile.readline()
print('End of file')
empInFile.close()