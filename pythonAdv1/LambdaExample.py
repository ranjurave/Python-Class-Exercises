#add = lambda a,b,c,d,e: a+b+c+d+e
numbers = [1,2,3,4,5,6,7,8,9]

squaredNum = list(map(lambda num: num * num, numbers))

print(squaredNum)