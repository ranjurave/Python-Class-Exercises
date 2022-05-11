myTuple = ("points",[1,2,3],(4,5,6))
thisTuple = (0,1,2,3,4,5,6,7,8)
if(9 not in thisTuple):
    thisTuple = thisTuple + (9,)

print(thisTuple)