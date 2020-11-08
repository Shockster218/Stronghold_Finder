from minecraftmath import calculator

def findSecondSuggestedThrow(startPosX, startPosZ, startAngle)
    hit = calculator.calculateHitRing(startPosX, startPosZ, startAngle)
    xSecThr, ySecThr = calculator.calculateSecondThrowCoordinates(hit)
    angleSecThr = calculator.calculateAngleAToB(startPosX, startPosZ, xSecThr, ySecThr)
    return (xSecThr, ySecThr, angleSecThr)

