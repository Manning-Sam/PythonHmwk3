def getAreaHouse():
    rooms={"bathroom":[8,7],
        "kitchen":[9,10],
        "bedroom1":[10,10],
        "bedroom2":[13,12]}
    areas=[]
    for key in rooms:
        area= rooms[key][0]*rooms[key][1]
        areas.append(area)
    totalArea = sum(areas)
    return totalArea
print(getAreaHouse())

def getcircumference():
    import math
    radius= float(input("What is the radius?:"))
    circumference = 2 * math.pi * radius
    return(circumference)
