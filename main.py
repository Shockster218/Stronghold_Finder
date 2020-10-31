import numpy as np
import pyperclip
import msvcrt
import curses

# hitCircle calculates where the first stronghold generation ring starts, where the player would "hit" it, moving directly forward
# and calculates the position to the second ender eye throw


def hitCircle(pX, pZ, angle):
    xHit = None
    yHit = None
    cos = np.cos(angle*np.pi/180)
    # if the stronghold is at the +X
    if cos >= 0:
        x = np.linspace(pX-10, 2700, 2700)
        a = np.tan(angle*np.pi/180)
        b = pZ - pX * a
        y = a*x + b
        for i in range(len(x)):
            if x[i]*x[i] + y[i]*y[i] >= 1408*1408:
                xHit = x[i]
                yHit = y[i]
                break
        pos1 = (xHit, yHit)
        x2 = np.linspace(xHit, xHit+100, 500)
        a2 = -1/np.tan(angle*np.pi/180)
        b2 = yHit - xHit * a2
        y2 = a2*x2 + b2
        for i in range(len(x2)):
            if abs(x2[i] - xHit)**2 + abs(y2[i] - yHit)**2 >= 42*42:
                xST = x2[i]
                yST = y2[i]
        pos2 = (xST, yST)
    # if the stronghold is at the -X
    else:
        x = np.linspace(pX+10, -2700, 2700)
        a = np.tan(angle*np.pi/180)
        b = pZ - pX * a
        y = a*x + b
        for i in range(len(x)):
            if x[i]*x[i] + y[i]*y[i] >= 1408*1408:
                xHit = x[i]
                yHit = y[i]
                break
        pos1 = (xHit, yHit)
        x2 = np.linspace(xHit, xHit+100, 500)
        a2 = -1/np.tan(angle*np.pi/180)
        b2 = yHit - xHit * a2
        y2 = a2*x2 + b2
        for i in range(len(x2)):
            if abs(x2[i] - xHit)**2 + abs(y2[i] - yHit)**2 >= 42*42:
                xST = x2[i]
                yST = y2[i]
        pos2 = (xST, yST)

    return (pos1, pos2)


def SecondThrowCoords(clip):
    # stabilishing the variables
    global firstThrowSet
    f3c0 = clip
    f3c0 = f3c0[42:]
    f3c0 = f3c0.split()
    px0 = float(f3c0[0])
    pz0 = float(f3c0[2])
    angle0 = float(f3c0[3]) % 360

    # translating minecraft angles to daily life cartesian angles
    if angle0 >= 0:
        angle0 = (angle0+90) % 360
    else:
        angle0 = (angle0-270) % 360

    # distance from origin
    distOrigin = np.sqrt(px0*px0 + pz0*pz0)
    # print("You're this far from the Origin: ", distOrigin)

    response = ""

    if distOrigin >= 1400:
        response = "Move 27 blocks perpendicularly to the Ender Eye flight direction and throw the second eye. Copy those coords for stronghold reading."

    else:
        circlePoint, secThrowPoint = hitCircle(px0, pz0, angle0)
        response = f'Suggested 2nd throw coords: ({secThrowPoint[0]} , {secThrowPoint[1]})'

    firstThrowSet = True


def StrongholdCoords(clip):
    f3c1 = clip
    f3c1 = f3c1[42:]
    f3c1 = f3c1.split()
    px1 = float(f3c1[0])
    pz1 = float(f3c1[2])
    angle1 = float(f3c1[3]) % 360

    # translating minecraft angles to daily life cartesian angles
    if angle1 >= 0:
        angle1 = (angle1+90) % 360
    else:
        angle1 = (angle1-270) % 360

    # calculating stronghold position
    a0 = np.tan(angle0*np.pi/180)
    a1 = np.tan(angle1*np.pi/180)
    b0 = pz0 - px0 * a0
    b1 = pz1 - px1 * a1
    pxS = (b1 - b0)/(a0 - a1)
    pzS = pxS * a0 + b0

    response = f'Stronghold location: ({pxS} , {pxZ})'
    addStrongholdCoords(response)


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.nodelay(1)
stdscr.keypad(True)
exit = False
newRun = True
firstThrowSet = False
netherSet = False
uInput = ""


def initWindow():
    global newRun
    global firstThrowSet
    global netherSet
    global uInput
    newRun = True
    firstThrowSet = False
    netherSet = False
    uInput = ""
    stdscr.clear()
    stdscr.addstr(0, 10, "Stronghold finder by Brandon Giannos aka Shockster_")
    stdscr.addstr(1, 10, "Coordinates for stronghold are read (x,z) and for nether (x,y,z)")
    stdscr.addstr(3, 0, "This runs nether coords: ")
    stdscr.addstr(5, 0, "Suggested 2nd throw coords: ")
    stdscr.addstr(6, 0, "Stronghold location: ")
    stdscr.move(8, 0)


def parseClipboard(clip):
    global newRun
    global firstThrowSet
    global netherSet
    if clip[1:21] == "execute in minecraft":
        if clip[22:32] == "the_nether" and netherSet == False and newRun == True:
            addNetherCoords(clip)
            newRun = False
            netherSet = True
        else:
            if netherSet == True:
                if firstThrowSet == True:
                    StrongholdCoords(clip)
                    netherSet = False
                    newRun = True
                else:
                    SecondThrowCoords(clip)
                    firstThrowSet = True


def addNetherCoords(clip):
    initWindow()
    f3 = clip
    f3 = f3[42:]
    f3 = f3.split()
    pX = int(round(float(f3[0])))
    pY = int(round(float(f3[1])))
    pZ = int(round(float(f3[2])))
    response = f'This runs nether coords: ({pX} , {pY}, {pZ}) '
    stdscr.addstr(3, 0, response)
    stdscr.move(8, 0)


def addSecondThrow(response):
    stdscr.addstr(5, 0, response)
    stdscr.move(8, 0)


def addStrongholdCoords(response):
    stdscr.addstr(6, 0, response)
    stdscr.move(8, 0)


def addUserInput(inp):
    global uInput
    global exit
    if inp == 10 and uInput == "exit":
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        stdscr.clear()
        exit = True
    elif inp == 8:
        uInput = uInput[:-1]
        stdscr.delch(8, len(uInput))
    elif chr(inp).isalpha():
        uInput = uInput + chr(inp)
        stdscr.addstr(8, 0, uInput)


initWindow()


while not exit:
    pyperclip.copy("")
    char = stdscr.getch()
    if char != -1:
        # reset key tilde
        if char == 96:
            initWindow()
        else:
            addUserInput(char)
    else:
        try:
            pyperclip.waitForNewPaste(0.1)
        except:
            pass
        else:
            clipboard = pyperclip.paste()
            parseClipboard(clipboard)
    stdscr.refresh()
