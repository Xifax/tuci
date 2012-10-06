#!/usr/bin/env python
# coding=utf-8

from time import sleep
import sys

from Tkinter import (
        Tk,
        TclError,
        Message,
        Text,
        CENTER,
)
import tkFont

from requests import (
        get,
        RequestException
)

# TODO: for global hotkeys checkout:
# http://www.schurpf.com/python/python-hotkey-module/
# http://kaizer.se/wiki/keybinder/
# http://svn.navi.cx/misc/trunk/python/evdev/evdev.py

if __name__ == '__main__':

    root = Tk()
    # Disable window decorations
    root.overrideredirect(True)

    try:
        # Try to get clipboard contents
        # NB: alternatives: paperclip
        contents = root.clipboard_get()
    except TclError:
        pass
    # Clipboard is not empty
    if contents:
        # Create notification
        note = Message(root, text=contents.encode('utf-8'), justify=CENTER, width=200, font=tkFont.Font(size=14))
        note.pack()

        # Define update method
        def add_item():
            sleep(1)
            # normalize clipboard contents
            try:
                # Perform request
                #reply = get(
                        #'http://suzu.herokuapp.com/add/%s' % contents
                        #).json
                #print reply.get('result'), reply.get('reason', '')
                pass
                # TODO: log|notify on reply
            except RequestException as e:
                print e
            # Close notification
            root.quit()
            # TODO: not quitting app -> wait for another hotkey event (Windows?)
            #root.withdraw()

        #r.withdraw();
        # Show notification for 2 seconds
        root.after(1000, add_item)
        # Start GUI
        root.mainloop()