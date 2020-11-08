import numpy as np
import pyperclip
import keyboard
import curses
import atexit
import time
import win32gui
import win32con
from config import config_file_read as r
from config import config_file_write as w
from math import calculator
from math import coordinate_finder as cf

configLoaded = r.initConfig()

try:
    hWnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowPos(hWnd, win32con.HWND_TOPMOST, 0, 0, r.WINDOW_WIDTH, r.WINDOW_HEIGHT, win32con.SWP_NOMOVE)
except:
    pass

# Calculates where the first stronghold generation ring starts, where the player would "hit" it, moving directly forward
# and calculates the position to the second ender eye throw
def calculateSecondThrowPosition(pX, pZ, angle):
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
        x2 = np.linspace(xHit, xHit+100, 500)
        a2 = -1/np.tan(angle*np.pi/180)
        b2 = yHit - xHit * a2
        y2 = a2 * x2 + b2
        for i in range(len(x2)):
            if abs(x2[i] - xHit)**2 + abs(y2[i] - yHit)**2 >= 42*42:
                xST = x2[i]
                yST = y2[i]
        pos = (xST, yST)
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
        x2 = np.linspace(xHit, xHit+100, 500)
        a2 = -1/np.tan(angle*np.pi/180)
        b2 = yHit - xHit * a2
        y2 = a2*x2 + b2
        for i in range(len(x2)):
            if abs(x2[i] - xHit)**2 + abs(y2[i] - yHit)**2 >= 42*42:
                xST = x2[i]
                yST = y2[i]
        pos = (xST, yST)

    return (pos)


def secondThrowCoords(clip):
    global posZFirThr, posXFirThr, angleFirThr
    f3Clip = clip[42:].split()
    posXFirThr = float(f3Clip[0])
    posZFirThr = float(f3Clip[2])
    angleFirThr = float(f3Clip[3]) % 360

    #This is wrong, this displays angle to stronghold not angle to suggested throw.
    #displayAngle = (angleFirThr, -180 + (angleFirThr - 180))[angleFirThr > 180]

    if angleFirThr >= 0:
        angleFirThr = (angleFirThr+90) % 360
    else:
        angleFirThr = (angleFirThr-270) % 360

    secThrowPoint = calculateSecondThrowPosition(posXFirThr, posZFirThr, angleFirThr)
    response = f'({int(secThrowPoint[0])} , {int(secThrowPoint[1])})'
    addSecondThrow(response)


def strongholdCoords(clip):
    global posXFirThr, posZFirThr, angleFirThr, posXSecThr, posZSecThr, angleSecThr
    f3Clip = clip[42:].split()
    posXSecThr = float(f3Clip[0])
    posZSecThr = float(f3Clip[2])
    angleSecThr = float(f3Clip[3]) % 360

    #This is good, displays angle to stronghold. Should move elsewhere during refactor
    # For exmaple Calculator.calculateAngleToStronghold
    displayAngle = (angleSecThr, -180 + (angleSecThr - 180))[angleSecThr > 180]

    if angleSecThr >= 0:
        angleSecThr = (angleSecThr+90) % 360
    else:
        angleSecThr = (angleSecThr-270) % 360

    # calculating stronghold position
    a0 = np.tan(angleFirThr*np.pi/180)
    a1 = np.tan(angleSecThr*np.pi/180)
    b0 = posZFirThr - posXFirThr * a0
    b1 = posZSecThr - posXSecThr * a1
    posXStrong = (b1 - b0)/(a0 - a1)
    posZStrong = posXStrong * a0 + b0

    # Stronghold 4,4 rule (stronghold stairs are on 4th block of chunk x and z)
    newPosXStrong = posXStrong - (posXStrong % 16) + (-12, 4)[int(posXStrong) % 16 > 0]
    newPosZStrong = posZStrong - (posZStrong % 16) + (-12, 4)[int(posZStrong) % 16 > 0]

    response = f'({int(newPosXStrong)} , {int(newPosZStrong)}) with angle {round(displayAngle, 1)}'
    addStrongholdCoords(response)


screen = curses.initscr()
screen.nodelay(1)
screen.keypad(True)
curses.noecho()
curses.cbreak()
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, 0)
curses.init_pair(2, curses.COLOR_GREEN, 0)
curses.init_pair(3, curses.COLOR_CYAN, 0)


exit = False
firstThrowSet = False
secondThrowSet = False
netherSet = False
netherPortal = "Not set!"
suggestedSecThrow = "Not set!"
strongholdLoc = "Not set!"


def initWindow(saveCoords=False):
    try:
        global secondThrowSet, firstThrowSet, netherSet, netherPortal, suggestedSecThrow, strongholdLoc
        firstThrowSet = (False, firstThrowSet)[saveCoords]
        secondThrowSet = (False, secondThrowSet)[saveCoords]
        netherSet = (False, netherSet)[saveCoords]
        netherPortal = ("Not set!", netherPortal)[saveCoords]
        suggestedSecThrow = ("Not set!", suggestedSecThrow)[saveCoords]
        strongholdLoc = ("Not set!", strongholdLoc)[saveCoords]
        screen.clear()
        screen.addstr(0, 15, "Stronghold finder by Brandon G aka Shockster_", curses.color_pair(3))
        screen.addstr(2, 2, "This runs nether coords: ")
        screen.addstr(("Not set!", netherPortal)[saveCoords], (curses.color_pair(1), curses.color_pair(2))[netherPortal != "Not set!"])
        screen.addstr(5, 2, "Suggested 2nd throw coords: ")
        screen.addstr(("Not set!", suggestedSecThrow)[saveCoords], (curses.color_pair(1), curses.color_pair(2))[suggestedSecThrow != "Not set!"])
        screen.addstr(6, 2, "Stronghold location: ")
        screen.addstr(("Not set!", strongholdLoc)[saveCoords], (curses.color_pair(1), curses.color_pair(2))[strongholdLoc != "Not set!"])
        screen.addstr(8, 2, f"[{r.RESET.upper()}] Reset coordinates | [{r.EXIT.upper()}] Exit program")
        screen.addstr(9, 2, f"[{r.LOCATE_FORTRESS.upper()}] Locate fortress command | [{r.LOCATE_STRONGHOLD.upper()}] Locate stronghold command")
        screen.refresh()
    except:
        pass


def parseClipboard(clip):
    global netherSet, firstThrowSet, secondThrowSet
    if clip[1:21] == "execute in minecraft":
        pyperclip.copy("")
        if clip[22:32] == "the_nether":
            if netherSet == False:
                initWindow()
                addNetherCoords(clip)
                netherSet = True
        else:
            if firstThrowSet == True:
                strongholdCoords(clip)
                secondThrowSet = True
            else:
                secondThrowCoords(clip)
                firstThrowSet = True


def addNetherCoords(clip):
    global netherPortal
    f3 = f3[42:].split()
    pX = int(round(float(f3[0])))
    pY = int(round(float(f3[1])))
    pZ = int(round(float(f3[2])))
    screen.addstr(3, 2, 'This runs nether coords: ')
    screen.addstr(f'({pX} , {pY}, {pZ})', curses.color_pair(2))
    netherPortal = f'({pX} , {pY}, {pZ})'


def addSecondThrow(response):
    global suggestedSecThrow
    screen.addstr(5, 2, "Suggested 2nd throw coords: ")
    screen.addstr(response, curses.color_pair(2))
    suggestedSecThrow = response


def addStrongholdCoords(response):
    global strongholdLoc
    screen.addstr(6, 2, "Stronghold location: ")
    screen.addstr(response, curses.color_pair(2))
    strongholdLoc = response


def sendFortressCommand():
    keyboard.press_and_release('t')
    time.sleep(0.05)
    keyboard.write('/locate fortress')
    keyboard.press_and_release('enter')


def sendStrongholdCommand():
    keyboard.press_and_release('t')
    time.sleep(0.05)
    keyboard.write('/locate stronghold')
    keyboard.press_and_release('enter')


def endProgram():
    global exit, hWnd
    try:
        win32gui.SetWindowPos(hWnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0)
    except:
        pass
    exit = True


def exit_handler():
    global screen
    w.SaveConfig(screen)


initWindow()
pyperclip.copy("")


keyboard.on_release_key(r.RESET, lambda x=None: initWindow())
keyboard.on_release_key(r.LOCATE_FORTRESS, lambda x=None: sendFortressCommand())
keyboard.on_release_key(r.LOCATE_STRONGHOLD, lambda x=None: sendStrongholdCommand())
keyboard.add_hotkey(r.EXIT, lambda: endProgram())
atexit.register(exit_handler)


while not exit:
    try:
        pyperclip.waitForNewPaste(0.1)
        clipboard = pyperclip.paste()
        parseClipboard(clipboard)
    except:
        pass

    if screen.getch() == curses.KEY_RESIZE:
        curses.resize_term(*screen.getmaxyx())
        initWindow(saveCoords=True)
