empInFile = open('EmpDetails.txt', 'r')
line = empInFile.readline()
empNum = 0
while(line!=''):
    empId = line
    empId.split('\n')
    empName = empInFile.readline()
    empName.split('\n')
    empPay = empInFile.readline()
    empPay.split('\n')
    empPayConverted = float(empPay)
    empDept = empInFile.readline()
    empDept.split('\n')
    empNum += 1
    print('Details of Employee ', empNum)
    print('------------------------------')
    print('Emp Id : ', empId)
    print('Employee Name : ',empName )
    print('Employee Pay : ',empPay )
    print('Dept : ',empDept)
    line = empInFile.readline()
empInFile.close()