#!/usr/bin/env python
# -*- coding: utf-8 -*-
__module_name__ = "mpv now playing"
__module_version__ = "1"
__module_description__ = "Displays mpv info"
__module_author__ = "kuehnelth"

import xchat
import ctypes, ctypes.wintypes
 
EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

titles = []
MAX_PATH = 260

def foreach_window(hwnd, lParam):
    if IsWindowVisible(hwnd):
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        if buff.value.startswith("mpv - "):
            titles.append(buff.value[6:])
    return True

def mpv_np(caller, callee, helper):
    global titles
    titles = []
    EnumWindows(EnumWindowsProc(foreach_window), 0)

    if len(titles) > 0:
        xchat.command("me now playing \x02%s\x0F in mpv" % titles[0])
    else:
        print("mpv is not runnung")
    return xchat.EAT_ALL

help_string = "Usage: /mpv"
xchat.hook_command(
    "mpv",
    mpv_np,
    help = help_string
)

print(help_string)
