numbers = [12,45,78,89,56,23,25,75]
# filter(function, iterable)
# lambda arguments : expression
evenNumList = list(filter(lambda x : x % 2 == 0 , numbers))

print(evenNumList)