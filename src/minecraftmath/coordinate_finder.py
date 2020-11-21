from minecraftmath import calculator
from system import window_management as wm

xFirThr = 0
zFirThr = 0
angleFirThr = 0

def findSecondSuggestedThrow(startPosX, startPosZ, startAngle):
    global xFirThr, zFirThr, angleFirThr
    xFirThr = startPosX
    zFirThr = startPosZ
    angleFirThr = startAngle
    inRing, distance = calculator.distanceFromOrigin(xFirThr, zFirThr)
    if inRing:
        return (0,0,calculator.convertToMinecraftAngle(angleFirThr, inRing=True), distance)
    else:
        xSugThr, zSugThr = calculator.calculateSecondThrowCoordinates(*calculator.calculateHitRing(xFirThr, zFirThr, angleFirThr))
        angleSugThr = calculator.calculateAngleAToB(xFirThr, zFirThr, xSugThr, zSugThr)
        return (xSugThr, zSugThr, angleSugThr)

def findStronghold(startPosX, startPosZ, startAngle):
    global xFirThr, zFirThr, angleFirThr
    xStronghold, zStronghold = calculator.calculateStrongholdCoordinates(xFirThr, zFirThr, angleFirThr, startPosX, startPosZ, startAngle)
    angleStronghold = calculator.calculateAngleAToB(startPosX, startPosZ, xStronghold, zStronghold)
    return (xStronghold, zStronghold, angleStronghold)

