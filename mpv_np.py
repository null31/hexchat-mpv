#!/usr/bin/env python
#encoding=utf-8

__module_name__ = "MPV now playing"
__module_version__ = "2.0"
__module_description__ = "Displays MPV info"
__module_author__ = "kuehnelth (v1.0) / null31 (v2.0)"

import socket
import json
from os.path import expanduser
import time
import hexchat

def get_property(s, property):
    cmd = {"command": ["get_property", property]}
    s.send(json.dumps(cmd).encode() + b'\n')
    res = json.loads(s.recv(4096).decode())
    if res["error"] != "success":
        return res["error"]
    else:
        return res["data"]

def mpv_np(caller, callee, helper):
    s = socket.socket(socket.AF_UNIX)
    try:
        s.connect(expanduser("~") + "/.config/mpv/socket")
    except:
        print("Socket error")
        return hexchat.EAT_ALL

    time_pos = time.strftime('%H:%M:%S', time.gmtime(get_property(s, "time-pos")))
    length   = time.strftime('%H:%M:%S', time.gmtime(get_property(s, "duration")))
    filename = get_property(s, "filename")
    render = get_property(s, "current-vo")
    version  = get_property(s, "mpv-version")

    hexchat.command("me now playing \x02%s\x0F [%s/%s] rendering with %s in %s" % (filename, time_pos, length, render, version))
    s.close()
    return hexchat.EAT_ALL

help_string = "Usage: /mpv \nSetup: Add 'input-ipc-server=~/.config/mpv/socket' to your ~/.config/mpv/mpv.conf"
hexchat.hook_command(
    "mpv",
    mpv_np,
    help = help_string
)

print(help_string)
