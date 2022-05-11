myList = [1,2,3,4,5,8,7]
# doubleList = [x*2 for x in myList]
# print(doubleList)

# myDict = {1:1, 2:4, 3:9, 4:16, 5:25}
#Dictionary Comprehension
doubleDict = {item:item * item for item in myList}
print(doubleDict)
