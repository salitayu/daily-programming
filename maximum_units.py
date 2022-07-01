def maximumUnits(boxTypes, truckSize):
    boxes = 0
    boxTypes.sort(key = lambda x:-x[1])
    for box, units in boxTypes:
        if truckSize > box:
            truckSize -= box
            boxes += box * units
        else:
            boxes += truckSize * units
            return boxes
    return boxes