import numpy as np
import pyperclip
import keyboard
import curses
import config_file_read
import config_file_write
import atexit
import time
# hitCircle calculates where the first stronghold generation ring starts, where the player would "hit" it, moving directly forward
# and calculates the position to the second ender eye throw

pz0 = 0
px0 = 0
angle0 = 0
pz1 = 0
px1 = 0
angle1 = 0

config_file_read.InitConfig()


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
        y2 = a2 * x2 + b2
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
    global pz0, px0, angle0
    f3c0 = clip
    f3c0 = f3c0[42:]
    f3c0 = f3c0.split()
    px0 = float(f3c0[0])
    pz0 = float(f3c0[2])
    angle0 = float(f3c0[3]) % 360

    if angle0 >= 0:
        angle0 = (angle0+90) % 360
    else:
        angle0 = (angle0-270) % 360

    circlePoint, secThrowPoint = hitCircle(px0, pz0, angle0)
    response = f'({int(secThrowPoint[0])} , {int(secThrowPoint[1])}) with angle {angle0}'
    addSecondThrow(response)


def StrongholdCoords(clip):
    global px0, pz0, angle0, px1, pz1, angle1
    f3c1 = clip
    f3c1 = f3c1[42:]
    f3c1 = f3c1.split()
    px1 = float(f3c1[0])
    pz1 = float(f3c1[2])
    angle1 = float(f3c1[3]) % 360

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

    response = f'({int(pxS)} , {int(pzS)}) with angle {angle1}'
    addStrongholdCoords(response)


stdscr = curses.initscr()
stdscr.nodelay(1)
stdscr.keypad(True)
curses.noecho()
curses.cbreak()
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, 0)
curses.init_pair(2, curses.COLOR_GREEN, 0)

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
        firstThrowSet = False
        secondThrowSet = False
        netherSet = False
        netherPortal = ("Not set!", netherPortal)[saveCoords]
        suggestedSecThrow = ("Not set!", suggestedSecThrow)[saveCoords]
        strongholdLoc = ("Not set!", strongholdLoc)[saveCoords]
        stdscr.clear()
        stdscr.addstr(0, 32, "Stronghold finder by Brandon Giannos aka Shockster_")
        stdscr.addstr(1, 5, "Coordinates for stronghold are read (x,z) and for nether (x,y,z). Please look at README.md for usage and FAQ.")
        stdscr.addstr(3, 0, "This runs nether coords: ")
        stdscr.addstr(("Not set!", netherPortal)[saveCoords], (curses.color_pair(1), curses.color_pair(2))[netherPortal != "Not set!"])
        stdscr.addstr(5, 0, "Suggested 2nd throw coords: ")
        stdscr.addstr(("Not set!", suggestedSecThrow)[saveCoords], (curses.color_pair(1), curses.color_pair(2))[suggestedSecThrow != "Not set!"])
        stdscr.addstr(6, 0, "Stronghold location: ")
        stdscr.addstr(("Not set!", strongholdLoc)[saveCoords], (curses.color_pair(1), curses.color_pair(2))[strongholdLoc != "Not set!"])
        stdscr.addstr(8, 0, f"[{config_file_read.RESET.upper()}] Reset coordinates | [{config_file_read.EXIT.upper()}] Exit program | [{config_file_read.LOCATE_FORTRESS.upper()}] Locate fortress command | [{config_file_read.LOCATE_STRONGHOLD.upper()}] Locate stronghold command")
        stdscr.refresh()
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
                StrongholdCoords(clip)
                secondThrowSet = True
            else:
                SecondThrowCoords(clip)
                firstThrowSet = True


def addNetherCoords(clip):
    global netherPortal
    f3 = clip
    f3 = f3[42:]
    f3 = f3.split()
    pX = int(round(float(f3[0])))
    pY = int(round(float(f3[1])))
    pZ = int(round(float(f3[2])))
    stdscr.addstr(3, 0, 'This runs nether coords: ')
    stdscr.addstr(f'({pX} , {pY}, {pZ})', curses.color_pair(2))
    netherPortal = f'({pX} , {pY}, {pZ})'


def addSecondThrow(response):
    global suggestedSecThrow
    stdscr.addstr(5, 0, "Suggested 2nd throw coords: ")
    stdscr.addstr(response, curses.color_pair(2))
    suggestedSecThrow = response


def addStrongholdCoords(response):
    global strongholdLoc
    stdscr.addstr(6, 0, "Stronghold location: ")
    stdscr.addstr(response, curses.color_pair(2))
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


def exit_handler():
    config_file_write.SaveConfig()


initWindow()
pyperclip.copy("")
atexit.register(exit_handler)


while not exit:
    if keyboard.is_pressed(config_file_read.RESET):
         initWindow()
    elif keyboard.is_pressed(config_file_read.EXIT):
        exit = True
    elif keyboard.is_pressed(config_file_read.LOCATE_FORTRESS):
        sendFortressCommand()
    elif keyboard.is_pressed(config_file_read.LOCATE_STRONGHOLD):
        sendStrongholdCommand()
    try:
        pyperclip.waitForPaste(0.1)
        clipboard = pyperclip.paste()
        parseClipboard(clipboard)
    except:
        pass
    if stdscr.getch() == curses.KEY_RESIZE:
        curses.resize_term(*stdscr.getmaxyx())
        initWindow(saveCoords=True)


