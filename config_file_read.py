from configparser import ConfigParser
from os import path
import config_file_write


parser = ConfigParser()


RESET = None
EXIT = None
LOCATE_FORTRESS = None
LOCATE_STRONGHOLD = None


def InitConfig():
    ParseConfig()


def ParseConfig():
    global RESET, EXIT, LOCATE_FORTRESS, LOCATE_STRONGHOLD
    if path.exists("config.ini"):
        parser.read('config.ini')
        temp = parser.get('Program Hotkeys', 'reset coordinates')
        if len(temp) == 1:
            RESET = temp
        else:
            RESET = config_file_write.DEFAULT_RESET
        temp = parser.get('Program Hotkeys', 'exit program') 
        if len(temp) == 1:
            EXIT = temp
        else:
            EXIT = config_file_write.DEFAULT_EXIT 
        temp = parser.get('Ingame Commands', 'locate fortress')
        if len(temp) == 1:
            LOCATE_FORTRESS = temp
        else:
            LOCATE_FORTRESS = config_file_write.DEFAULT_LOCATE_FORTRESS
        temp = parser.get('Ingame Commands', 'locate stronghold')
        if len(temp) == 1:
            LOCATE_STRONGHOLD = temp
        else:
            LOCATE_STRONGHOLD = config_file_write.DEFAULT_LOCATE_STRONGHOLD
    else:
        config_file_write.WriteDefaultConfig()
        SetDefaultHotkeys()

def SetDefaultHotkeys():
    global RESET, EXIT, LOCATE_FORTRESS, LOCATE_STRONGHOLD
    RESET = config_file_write.DEFAULT_RESET
    EXIT = config_file_write.DEFAULT_EXIT
    LOCATE_FORTRESS = config_file_write.DEFAULT_LOCATE_FORTRESS
    LOCATE_STRONGHOLD = config_file_write.DEFAULT_LOCATE_STRONGHOLD
        