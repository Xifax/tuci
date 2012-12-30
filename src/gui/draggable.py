#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Allow for dragging widgets by mouse
"""

# external #
from PySide.QtCore import QObject

class Draggable(QObject):

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x, y = event.globalX(), event.globalY()
        x_w, y_w = self.offset.x(), self.offset.y()
        self.move(x - x_w, y - y_w)


