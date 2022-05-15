def bothargs_kwargs(*args,**kwargs):
    print(args)
    print(kwargs)

bothargs_kwargs(1,2,3,4,5, name = "Jack", age = 50)

mytuple = (45,56,78)
myDict = {"name":"Todd","age":12}
bothargs_kwargs(mytuple,**myDict)