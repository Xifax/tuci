#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Main GUI widget
"""

# external #
from PySide.QtGui import (
        QDialog,
        QApplication,
        QHBoxLayout,
)
from PySide.QtCore import Qt

# own #
from text import Text
from info import Info
from composer import Composer
from draggable import Draggable


# see: http://forum.meego.com/showthread.php?t=1543


class Widget(QDialog, Composer):

    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        # Initialize base gui widgets and objects
        self.text, self.info = Text(), Info()
        self.clip = QApplication.clipboard()

        # Initialize composition
        self.compose({
            QHBoxLayout(): [self.text, self.info]
        })

        # Initialize events
        self.clip.dataChanged.connect(self.clipped)

        # Initialize styles


    def clipped(self):
        """Update view on clipboard change"""
        # 1. TODO: Parse clipboard contents
        # 2. Update view
        self.text.update(self.clip.text())


    def mouseMoveEvent(self, event):
        if self.moving:
            self.move(event.globalPos()-self.offset)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moving = True
            self.offset = event.pos()


    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moving = False

