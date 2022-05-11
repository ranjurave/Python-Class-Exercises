def GlobalVsLocal():
    global myVar
    myVar = 10
    print(myVar)

# myVar=5
# print(myVar)
GlobalVsLocal()
print(myVar)