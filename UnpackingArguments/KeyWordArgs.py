#Unpacked inside the function
def named(**kwargs):
    print(type(kwargs))
    print(kwargs)
named(name = "Bob", age=25)

#Unpacked in the function call
people = {"name" :"Bob", "age":25}
def named(name,age):
    print(name, age)
named(**people)

friends = {"name" :"Rolf", "age":35}
def friendsList(**kwargs):
    print(kwargs)
    print(kwargs["name"])
friendsList(**friends)