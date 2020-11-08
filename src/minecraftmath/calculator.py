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


def calculateAngleAToB(aX, aY, bX, bY):
    angle = np.arctan2(ax - ay, bx - by) * (180.0 / Math.PI)
    angle = (angle, -180 + (angle - 180))[angle > 180]
    return angle
    