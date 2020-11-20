import win32gui
import win32con
import curses
from minecraftmath import calculator
from config import config_file_read as r
from config import config_file_write as w
from system import clipboard_parser as parser

hWnd = None
screen = None
nether = None
suggestion = None
stronghold = None
close = False
netherStatic = "This runs nether coords: "
suggestionStatic = "Suggested 2nd throw: "
strongholdStatic = "Stronghold location: "


def init():
    global hWnd
    try:
        hWnd = win32gui.GetForegroundWindow()
        win32gui.SetWindowPos(hWnd, win32con.HWND_TOPMOST, 0, 0, r.WINDOW_WIDTH, r.WINDOW_HEIGHT, win32con.SWP_NOMOVE)
    except:
        pass
    initScreen()
    drawScreen()


def initScreen():
    global screen
    screen = curses.initscr()
    screen.nodelay(1)
    screen.keypad(True)
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, 0)
    curses.init_pair(2, curses.COLOR_GREEN, 0)
    curses.init_pair(3, curses.COLOR_CYAN, 0)


def drawScreen(redraw=False):
    global nether, suggestion, stronghold
    nether = ("Not set!", nether)[redraw]
    suggestion = ("Not set!", suggestion)[redraw]
    stronghold = ("Not set!", stronghold)[redraw]
    screen.clear()
    screen.addstr(0, 15, "Stronghold finder by Brandon G aka Shockster_", curses.color_pair(3))
    screen.addstr(2, 2, netherStatic)
    screen.addstr(("Not set!", nether)[redraw], (curses.color_pair(1), curses.color_pair(2))[nether != "Not set!"])
    screen.addstr(4, 2, suggestionStatic)
    screen.addstr(("Not set!", suggestion)[redraw], (curses.color_pair(1), curses.color_pair(2))[suggestion != "Not set!"])
    screen.addstr(5, 2, strongholdStatic)
    screen.addstr(("Not set!", stronghold)[redraw], (curses.color_pair(1), curses.color_pair(2))[stronghold != "Not set!"])
    screen.addstr(7, 2, f"[{r.RESET.upper()}] Reset coordinates | [{r.EXIT.upper()}] Exit program")
    screen.addstr(8, 2, f"[{r.LOCATE_FORTRESS.upper()}] Locate fortress command | [{r.LOCATE_STRONGHOLD.upper()}] Locate stronghold command")
    screen.refresh()
    if not redraw:
        parser.clear()


def addNether(x, y, z):
    global nether
    nether = f'X:{x}, Y:{y}, Z:{z}'
    screen.addstr(2, 2, netherStatic)
    screen.addstr(nether, curses.color_pair(2))
    screen.refresh()


def addSuggestion(x, z, angle, distance=0):
    global suggestion
    screen.addstr(4, 2, suggestionStatic)
    if x == 0:
        suggestion = f'Turn right to angle: {round(angle, 1)}. Run 45s-1m. Throw 2nd eye.'
        screen.addstr(suggestion, curses.color_pair(2))
    else:
        suggestion = f'X:{int(round(x))}, Z:{int(round(z))} with angle {round(angle, 1)}'
        screen.addstr(suggestion, curses.color_pair(2))
    screen.refresh()


def addStronghold(x, z, angle):
    global stronghold
    stronghold = f'X:{int(round(x))}, Z:{int(round(z))} with angle {round(angle, 1)}'
    screen.addstr(5, 2, strongholdStatic)
    screen.addstr(stronghold, curses.color_pair(2))
    screen.refresh()


def getch():
    return screen.getch()


def positionMouse():
    screen.move(8,61)


def getmaxyx():
    return screen.getmaxyx()


def checkExit():
    return close