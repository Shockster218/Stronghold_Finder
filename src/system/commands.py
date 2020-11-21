import win32gui
import win32con
import keyboard
import time
from system import window_management as wm
from config import config_file_write as w

def onExit():
    try:
        win32gui.SetWindowPos(wm.hWnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0)
    except:
        pass
    w.SaveConfig(wm.screen)
    wm.close = True


def reset():
    wm.drawScreen()


def findFortress():
    keyboard.press_and_release('t')
    time.sleep(0.05)
    keyboard.write('/locate fortress')
    keyboard.press_and_release('enter')


def findStronghold():
    keyboard.press_and_release('t')
    time.sleep(0.05)
    keyboard.write('/locate stronghold')
    keyboard.press_and_release('enter')
