import pyperclip
import keyboard
import curses
import atexit
import time
from system import window_management as wm
from config import config_file_read as r
from system import clipboard_parser as parser

exit = False

r.init()
wm.init()
pyperclip.copy("")

keyboard.on_release_key(r.RESET, lambda x=None: wm.drawScreen())
#keyboard.on_release_key(r.LOCATE_FORTRESS, sendFortressCommand())
#keyboard.on_release_key(r.LOCATE_STRONGHOLD, sendStrongholdCommand())
keyboard.add_hotkey(r.EXIT, lambda x=None: wm.onExit())

while not exit:
    try:
        pyperclip.waitForNewPaste(0.1)
        clipboard = pyperclip.paste()
        parser.handleClipboard(clipboard)
    except:
        pass

    if wm.getch() == curses.KEY_RESIZE:
        curses.resize_term(*wm.getmaxyx())
        wm.drawScreen(redraw=True)

    if wm.checkExit():
        exit = True
