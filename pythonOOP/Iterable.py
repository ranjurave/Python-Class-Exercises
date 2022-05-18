myList = [234,546,67,889]

myIter = iter(myList)

print(next(myIter))
print(next(myIter))

print(myIter.__next__())


