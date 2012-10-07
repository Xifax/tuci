tuci
====

Tiny thingamabob for consuming suzu-web api. Will be probably rewritten in QT (if it actully installs using pip, eh).

## Inane requirements for Windows (as always):

* pywin32: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20217/pywin32-217.win32-py2.7.exe/download
* cx_freeze: http://sourceforge.net/projects/cx-freeze/files/latest/download

## Workflow

In case single items should be added:

1. Launch app
2. Copy item
3. Press Ctrl+Alt+A to add it to web-app DB
4. Repeat steps 2 to 3
5. Ctrl+Alt+Q (or middle click on notification) to quit

In case an example and corresponding items should be added:

1. Launch app
2. Copy example (if not autocopied)
3. Ctrl+Alt+E to set active example
4. Ctrl+Alt+A to add item corresponding to active example and restore example in clipboard
5. Ctrl+Alt+S to add example and corresponding items to web-app DB
6. Ctrl+Alt+Q to quit

## P.S.

As of now it is ugly (and code is smelly), but usable (at least, in windows). Hooray!

## TODO:

0. FREEEZE (or at the very least try to) as standalone exe, w/e
1. Port to PyQT|PySide
2. Show&hide notification on action
3. Allow to move notification
4. Reimplement hotkey hooker (pyhk is VERY laggy) to allow for single thread handling
5. Write log
6. Allow drag & drop
7. Options and stuff
8. Pretty fonts (should be number 1, but Tkinter, yeah)
9. CAN I HAZ makefile with autodownloaded dependencies..?
