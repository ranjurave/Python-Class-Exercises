print ("Randome number reader")
print ("=====================")
total = 0
numCount = 0
infile = open('RandomNumbers.txt','r')
for line in infile:
    num = int(line)
    total += num
    numCount += 1
infile.close()
print(f'There are {numCount} random numbers '
      f'and their total is {total}')