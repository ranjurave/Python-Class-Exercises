#Add nubmers from 1 to 100 to a file
numberOutFile = open('numbers.txt', 'w')
for x in range(1,101):
    numberOutFile.write(str(x)+'\n')
numberOutFile.close()