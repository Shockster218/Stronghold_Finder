import numpy as np

def calculateHitRing(startPosX, startPosZ, startAngle):
    xHit = None
    yHit = None
    cos = np.cos(startAngle*np.pi/180)
    # if the stronghold is at the +X
    if cos >= 0:
        x = np.linspace(startPosX-10, 2700, 2700)
        a = np.tan(startAngle*np.pi/180)
        b = startPosZ - startPosX * a
        y = a*x + b
        for i in range(len(x)):
            if x[i]*x[i] + y[i]*y[i] >= 1408*1408:
                xHit = x[i]
                yHit = y[i]
                break
        hit = (xHit, yHit, startAngle)
    # if the stronghold is at the +X
    else:
        x = np.linspace(startPosX+10, -2700, 2700)
        a = np.tan(startAngle*np.pi/180)
        b = startPosZ - startPosX * a
        y = a*x + b
        for i in range(len(x)):
            if x[i]*x[i] + y[i]*y[i] >= 1408*1408:
                xHit = x[i]
                yHit = y[i]
                break
        hit = (xHit, yHit, startAngle)
    return (hit)


def calculateSecondThrowCoordinates(xHit, yHit, angle):
    x = np.linspace(xHit, xHit+100, 500)
    a = -1/np.tan(angle*np.pi/180)
    b = yHit - xHit * a
    y = a * x + b
    for i in range(len(x)):
        if abs(x[i] - xHit)**2 + abs(y[i] - yHit)**2 >= 42*42:
            xSecThr = x[i]
            zSecThr = y[i]
    return (xSecThr, zSecThr)


def calculateStrongholdCoordinates(xFirThr, zFirThr, angleFirThr, xSecThr, zSecThr, angleSecThr):
    a0 = np.tan(angleFirThr*np.pi/180)
    a1 = np.tan(angleSecThr*np.pi/180)
    b0 = zFirThr - xFirThr * a0
    b1 = zSecThr - xSecThr * a1
    xStronghold = (b1 - b0)/(a0 - a1)
    zStronghold = xStronghold * a0 + b0
    xStronghold = xStronghold - (xStronghold % 16) + ((-12, 4)[int(xStronghold) % 16 > 0])
    zStronghold = zStronghold - (zStronghold % 16) + ((-12, 4)[int(zStronghold) % 16 > 0])
    return (xStronghold, zStronghold)


def calculateAngleAToB(aX, aZ, bX, bZ):
    angle = np.arctan2(aX-bX, aZ-bZ)
    angle = -1 * (angle / np.pi) * 360 / 2 + 180
    angle = convertToMinecraftAngle(angle)
    return angle


def roundNetherCoordinates(x, y, z):
    return (int(round(x)), int(round(y)), int(round(z)))


def distanceFromOrigin(x, z):
    distance = np.sqrt(x*x + z*z)
    if distance >= 1400:
        return (True, distance)
    else:
        return (False, distance)


def convertToMinecraftAngle(angle, inRing=False):
    a = (angle, angle - 30)[inRing]
    a = (a, -180 + (a - 180))[a > 180]
    return a
