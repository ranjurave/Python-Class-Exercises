# Read and add all numbers in file
numbersInFile = open('numbers.txt', 'r')
total = 0
for line in numbersInFile:
    print(line)
    line.split("\n")
    total = total + int(line)
print(total)
numbersInFile.close()