#nubmers from 0 to 100
numberOutFile = open('numbers.txt', 'w')
for x in range(1,101):
    numberOutFile.write(str(x)+'\n')
numberOutFile.close()