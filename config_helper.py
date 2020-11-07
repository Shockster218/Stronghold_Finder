import config_file_read as r
import config_file_write as w
import win32gui

def getWindowWidth():
    try:
        rect = win32gui.GetWindowRect(win32gui.GetForegroundWindow())
    except:
        pass
    if rect is not None:
        return str(rect[2] - rect[0])
    else:
        return r.WINDOW_WIDTH

def getWindowHeight():
    try:
        rect = win32gui.GetWindowRect(win32gui.GetForegroundWindow())
    except:
        pass
    if rect is not None:
        return str(rect[3] - rect[1])
    else:
        return r.WINDOW_HEIGHT
    
