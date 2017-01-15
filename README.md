# XChat/Hexchat mpv now playing script

Forked from kuehnelth/xchat_mpv_np.
>Fixed the length property.

>Added render property.

Usage:
======

`/mpv` - Show information about currently open file in mpv

Setup:
======

`xchat_mpv_np.py` uses the mpv [JSON IPC Protocol](http://mpv.io/manual/stable/#json-ipc).
To enable it, add the following line to `~/.mpv/config`
    input-unix-socket=~/.mpv/socket

`xchat_mpv_np_windows.py` works without any setup.

LICENSE
=======
                DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                        Version 2, December 2004
    
    Everyone is permitted to copy and distribute verbatim or modified
    copies of this license document, and changing it is allowed as long
    as the name is changed.
    
                DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
       TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

      0. You just DO WHAT THE FUCK YOU WANT TO.
    
