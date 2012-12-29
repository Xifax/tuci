# -*- coding=utf-8 -*-
"""
Main application script. Console-less version.
"""

# internal #
import sys

# external #
from PySide.QtGui import (
        QApplication,
        QIcon
)

# own #
from src.gui.widget import Widget

def main():
    app = QApplication(sys.argv)

    widget = Widget()
    widget.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
