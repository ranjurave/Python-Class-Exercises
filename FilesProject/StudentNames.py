#Student names save to file
numberOfStudents = int(input("Enter number of students "))
studentOutFile = open('StudentDetails.txt', 'a')
for x in range(numberOfStudents):
    print('Enter student ', x+1, ' name')
    sName = input()
    studentOutFile.write(sName + '\n')
studentOutFile.close()
print('Names entered in file')