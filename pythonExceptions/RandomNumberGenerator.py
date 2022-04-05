import random
print("Random number generator")
print("=======================")
totalNumbers = int(input("Enter required random numbers : "))
outfile = open('RandomNumbers.txt','w')
for x in range(totalNumbers):
    randomNumber = random.randrange(1,500)
    outfile.write(str(randomNumber)+'\n')
outfile.close()
print("Random numbers saved to file")