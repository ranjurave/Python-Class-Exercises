def dict_product(num):
    total = 1
    for val in num.values():
        total = total * val
    return total

num={"a":1,"b":3,"c":5,"d":9}

print(dict_product(num))