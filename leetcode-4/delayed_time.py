def findDelayedArrivalTime(arrivalTime: int, delayedTime: int) -> int:
    if arrivalTime + delayedTime >= 24:
        if arrivalTime + delayedTime == 24:
            return 0
        else:
            return arrivalTime + delayedTime - 24
    else:
        return arrivalTime + delayedTime
    
print(findDelayedArrivalTime(15, 5))
print(findDelayedArrivalTime(13, 11))
print(findDelayedArrivalTime(24, 12))
