#!/usr/bin/env python
# coding=utf-8

from time import sleep
import sys

from Tkinter import (
        StringVar,
        Frame,
        Tk,
        TclError,
        Message,
        Text,
        CENTER,
        Toplevel,
)
import tkFont

from requests import (
        get,
        RequestException
)

from src.hotkeys import GlobalHotkeyManager

# TODO: for global hotkeys checkout:
# http://www.schurpf.com/python/python-hotkey-module/
# http://kaizer.se/wiki/keybinder/
# http://svn.navi.cx/misc/trunk/python/evdev/evdev.py


class Application(Frame):
    def add_item(self):
        contents = None
        try:
            # Try to get clipboard contents
            # NB: alternatives: paperclip
            #contents = root.clipboard_get()
            
            #if 'normal' != self.master.state():
            #self.master.update()
            #self.master.deiconify()
            contents = self.master.clipboard_get()
            self.copied.set('Adding: \n' + contents)
        except TclError:
            # Clipboard is empty
            pass
            self.copied.set('Empty')
        # Clipboard is not empty
        if contents:
            # In case of very fast response
            sleep(1)
            try:
                # Perform request
                reply = get(
                        'http://suzu.herokuapp.com/add/%s' % contents
                        ).json
                #print reply.get('result'), reply.get('reason', '')
                # TODO: log|notify on reply
                self.copied.set(
                    'Result: %s\nError: %s' %
                    (reply.get('result'), reply.get('reason', 'None'))
                    )
            except RequestException as e:
                print e
            #self.after(1000, self.master.withdraw)
            #self.master.deiconify()

    def createWidgets(self):
        self.copied = StringVar()
        self.message = Message(
            self,
            textvariable=self.copied,
            justify=CENTER,
            width=500,
            font=tkFont.Font(size=16),
            bg='black',
            fg='white',
            )
        self.message.pack()
        #self.top = Toplevel()
        #self.top.lift(aboveThis=self.master)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        # Quit on middle click
        self.master.bind('<Button-2>', quit)
        self.pack()
        self.createWidgets()
        # Bind global hotkey
        self.hooker = GlobalHotkeyManager(self.add_item , 'A')
        # Should terminate with GUI
        self.hooker.setDaemon(True)
        self.hooker.start()

if __name__ == '__main__':
  
    root = Tk()
    #root.withdraw()
    # Disable window decorations
    root.overrideredirect(True)
    # Set transparency
    root.attributes("-alpha", 0.80)
    # Always on top
    root.attributes("-topmost", 1)
    # Position window in left top corner
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    #root.geometry('+%s+%s' % (width, height)) 
    root.geometry('+%s+%s' % (10, 50)) 
    # (..I should really switch to QT..)
    app = Application(master=root)
    app.mainloop()
    root.destroy()
