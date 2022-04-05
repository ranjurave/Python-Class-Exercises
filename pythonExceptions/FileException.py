FileName = input("Enter file name : ")
total = 0.0
try:
    infile = open(FileName, 'r')
    for line in infile:
        amount = float(line)
        total += amount
    infile.close()
    print("Total amount is : ", total)
except IOError:
    print("Error : File not found:")
except ValueError as err:
    print(err)
else:
    print("No exceptions")
finally:
    print("try except finished")