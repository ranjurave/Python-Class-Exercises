def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total

def apply(*args, operator):
    if operator == '*':
        return multiply(*args)

    if operator == '+':
        return sum(args)

print(apply(1,2,3,4, operator = '+'))
print(apply(1,2,3,4, operator = '*'))
