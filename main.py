import numpy as np
import pyperclip
import keyboard
import curses

# hitCircle calculates where the first stronghold generation ring starts, where the player would "hit" it, moving directly forward
# and calculates the position to the second ender eye throw

pz0 = 0
px0 = 0
angle0 = 0
pz1 = 0
px1 = 0
angle1 = 0


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
    global pz0
    global px0
    global angle0
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
    response = f'({int(secThrowPoint[0])} , {int(secThrowPoint[1])})'
    addSecondThrow(response)


def StrongholdCoords(clip):
    global px0
    global px0
    global angle0
    global pz1
    global px1
    global angle1
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

    response = f'({int(pxS)} , {int(pzS)})'
    addStrongholdCoords(response)


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.nodelay(1)
stdscr.keypad(True)
exit = False
firstThrowSet = False
secondThrowSet = False
netherSet = False
uInput = ""
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, 0)
curses.init_pair(2, curses.COLOR_GREEN, 0)


def initWindow():
    global secondThrowSet
    global firstThrowSet
    global netherSet
    global uInput
    firstThrowSet = False
    secondThrowSet = False
    netherSet = False
    uInput = ""
    stdscr.clear()
    stdscr.addstr(0, 32, "Stronghold finder by Brandon Giannos aka Shockster_")
    stdscr.addstr(1, 5, "Coordinates for stronghold are read (x,z) and for nether (x,y,z). Please look at README.md for usage and FAQ.")
    stdscr.addstr(3, 0, "This runs nether coords: ")
    stdscr.addstr("Not set!", curses.color_pair(1))
    stdscr.addstr(5, 0, "Suggested 2nd throw coords: ")
    stdscr.addstr("Not set!", curses.color_pair(1))
    stdscr.addstr(6, 0, "Stronghold location: ")
    stdscr.addstr("Not set!", curses.color_pair(1))
    stdscr.addstr(8, 0, "Input: ")
    stdscr.addstr(10, 0, "Hit [`] or Type 'reset' to reset coordinates  |  Type 'exit' to close the program")
    stdscr.move(8, 7)
    stdscr.refresh()


def parseClipboard(clip):
    global netherSet
    global firstThrowSet
    global secondThrowSet
    if secondThrowSet == True:
        initWindow()
    if clip[1:21] == "execute in minecraft":
        if clip[22:32] == "the_nether":
            if netherSet == False:
                if firstThrowSet == True:
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
    f3 = clip
    f3 = f3[42:]
    f3 = f3.split()
    pX = int(round(float(f3[0])))
    pY = int(round(float(f3[1])))
    pZ = int(round(float(f3[2])))
    stdscr.addstr(3, 0, 'This runs nether coords: ')
    stdscr.addstr(f'({pX} , {pY}, {pZ})', curses.color_pair(2))
    stdscr.move(8, 7)


def addSecondThrow(response):
    stdscr.addstr(5, 0, "Suggested 2nd throw coords: ")
    stdscr.addstr(response, curses.color_pair(2))
    stdscr.move(8, 7)


def addStrongholdCoords(response):
    stdscr.addstr(6, 0, "Stronghold location: ")
    stdscr.addstr(response, curses.color_pair(2))
    stdscr.move(8, 7)


def addUserInput(inp):
    global uInput
    global exit
    if inp == 10:
        if uInput.lower() == "exit":
            stdscr.keypad(False)
            curses.echo()
            curses.endwin()
            stdscr.clear()
            exit = True
        elif uInput.lower() == "reset":
            initWindow()
    elif inp == 8:
        uInput = uInput[:-1]
        stdscr.delch(8, 7 + len(uInput))
    elif chr(inp).encode('utf-8').isalpha():
        uInput = uInput + chr(inp)
        stdscr.addstr(8, 0, f'Input: {uInput}')


initWindow()
pyperclip.copy("")


while not exit:
    char = stdscr.getch()
    if char != -1:
        addUserInput(char)
    else:
        if keyboard.is_pressed('g'):
            initWindow()
        try:
            pyperclip.waitForPaste(0.1)
        except:
            pass
        else:
            clipboard = pyperclip.paste()
            parseClipboard(clipboard)
            pyperclip.copy("")
    stdscr.refresh()
