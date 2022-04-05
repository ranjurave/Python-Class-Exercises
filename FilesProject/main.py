#Open file program

employeeFile = open('D:\employeeDetails.txt', 'w')
employeeFile.write("Daniel\n")
employeeFile.write('Maria\n')
employeeFile.write('Joe\n')
employeeFile.close()
empFileOutput = open('D:\employeeDetails.txt', 'r')
line1 =empFileOutput.readline()
line1 = line1.rstrip('\n')
line2 = empFileOutput.readline()
line2.split("\n")
empFileOutput.close()
print(line1, line2)