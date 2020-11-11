import numpy as np

def calculateHitRing(startPosX, startPosZ, startAngle):
    xHit = None
    yHit = None
    cos = np.cos(angle*np.pi/180)
    # if the stronghold is at the +X
    if cos >= 0:
        x = np.linspace(startPosX-10, 2700, 2700)
        a = np.tan(angle*np.pi/180)
        b = startPosZ - startPosX* a
        y = a*x + b
        for i in range(len(x)):
            if x[i]*x[i] + y[i]*y[i] >= 1408*1408:
                xHit = x[i]
                yHit = y[i]
                break
        hit = (xHit, yHit, angle)
    # if the stronghold is at the +X
    else:
        x = np.linspace(startPosX+10, -2700, 2700)
        a = np.tan(angle*np.pi/180)
        b = startPosZ - startPosX * a
        y = a*x + b
        for i in range(len(x)):
            if x[i]*x[i] + y[i]*y[i] >= 1408*1408:
                xHit = x[i]
                yHit = y[i]
                break
        hit = (xHit, yHit, angle)
    return hit
        

def calculateSecondThrowCoordinates(xHit, yHit, angle):
    x = np.linspace(xHit, xHit+100, 500)
    a = -1/np.tan(angle*np.pi/180)
    b = yHit - xHit * a
    y = a * x + b
    for i in range(len(x2)):
         if abs(x[i] - xHit)**2 + abs(y[i] - yHit)**2 >= 42*42:
            xSecThr = x[i]
            ySecThr = y[i]
    return (xSecThr, ySecThr)


def calculateStrongholdCoordinates(xFirThr, zFirThr, angleFirThr, xSecThr, zSecThr, angleSecThr):
    if angleSecThr >= 0:
        angleSecThr = (angleSecThr+90) % 360
    else:
        angleSecThr = (angleSecThr-270) % 360

    # calculate stronghold position
    a0 = np.tan(angleFirThr*np.pi/180)
    a1 = np.tan(angleSecThr*np.pi/180)
    b0 = zFirThr - xFirThr * a0
    b1 = zSecThr - xSecThr * a1
    xStronghold = (b1 - b0)/(a0 - a1)
    zStronghold = xStronghold * a0 + b0
    return (xStronghold, zStronghold)


def calculateAngleAToB(aX, aY, bX, bY):
    angle = np.arctan2(ax - ay, bx - by)
    angle = (-(angle / np.pi) * 360) / 2 + 180
    angle = (angle, -180 + (angle - 180))[angle > 180]
    return angle
    

def roundNetherCoordinates(x, y, z):
    return (int(round(x)), int(round(y)), int(round(z)))