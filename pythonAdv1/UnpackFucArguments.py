def multiply(a,b):
    return a*b

num = {"a":4, "b":32}

#print(multiply(num["a"],num["b"]))
#print(multiply( a = num["a"], b = num["b"]))

print(multiply(**num))