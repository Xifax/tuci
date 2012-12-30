#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Info popup (additional, aside from translation)
"""

# external #
from PySide.QtGui import (
        QWidget,
)

# own #
from composer import Composer

class Info(QWidget, Composer):

    def __init__(self, parent=None):
        super(Info, self).__init__(parent)
