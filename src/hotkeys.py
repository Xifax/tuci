# -*- coding: utf-8 -*-

import ctypes
from ctypes import wintypes
import win32con

from threading import Thread, Event

class GlobalHotkeyManager(Thread):
    def __init__(self, function, key):
        Thread.__init__(self)
        self.function = function
        self.key = key

        self.byref = ctypes.byref
        self.user32 = ctypes.windll.user32

        self.event = Event()

        #TODO: add configurable modifiers & multiple hotkeys

        self.id = 1
        self.modifiers = win32con.MOD_CONTROL + win32con.MOD_ALT
        self.vk = ord(self.key)

    def registerHotkey(self):
        if not self.user32.RegisterHotKey(None, self.id, self.modifiers, self.vk):
            print 'Unable to register id', id, '\n'
        else:
            print 'registered ' + str(self.id) + ' ' + self.key + '\n'

    def messageLoop(self):
        try:
            msg = wintypes.MSG()
            #while self.user32.GetMessageA (self.byref (msg), None, 0, 0) != 0 and not self.event.is_set():
            while self.user32.GetMessageA (self.byref (msg), None, 0, 0) != 0:
                if msg.message == win32con.WM_HOTKEY:
                    self.function()

            self.user32.TranslateMessage (self.byref (msg))
            self.user32.DispatchMessageA (self.byref (msg))

        finally:
            self.unregisterHotkeys()
            print 'Hotkey unregistered\n'

    def unregisterHotkeys(self):
        self.user32.UnregisterHotKey(None, self.id)

    def run(self):
        self.registerHotkey()
        self.messageLoop()

    def stop(self):
        self.event.set()
