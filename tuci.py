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

#import src.pyhk
from src.pyhk import pyhk

# TODO: for global hotkeys checkout:
# http://www.schurpf.com/python/python-hotkey-module/
# http://kaizer.se/wiki/keybinder/
# http://svn.navi.cx/misc/trunk/python/evdev/evdev.py

def fun():

if __name__ == '__main__':
  
    
    # Bind global hotkey
    #hot = pyhk.pyhk()
    hot = pyhk()
    hot.addHotkey(['Ctrl', 'Alt', '1'], fun)
    hot.start()

    root = Tk()
    # Disable window decorations
    root.overrideredirect(True)
    # Position window in left top corner
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    #root.geometry('+%s+%s' % (width, height)) 
    root.geometry('+%s+%s' % (10, 50)) 
    # (..I should really switch to QT..)

    try:
        # Try to get clipboard contents
        # NB: alternatives: paperclip
        contents = root.clipboard_get()
    except TclError:
        # Clipboard is empty
        pass
    # Clipboard is not empty
    if contents:
        # Create notification
        note = Message(
            root,
            text='New item: ' + contents.encode('utf-8'),
            justify=CENTER,
            width=200,
            font=tkFont.Font(size=16),
            bg='black',
            fg='white',
            )
        note.pack()

        # Define update method
        def add_item():
            sleep(2)
            # normalize clipboard contents
            try:
                #print contents
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
