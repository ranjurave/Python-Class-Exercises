numbers = [1,2,3,4,5,6,7,8,9]

def numberSquared(num):
    return num * num

squaredNum = list(map(numberSquared, numbers))

print(squaredNum)