#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    QT layouts and widgets composer
"""

# external #
from PySide.QtCore import (
        QObject,
        Qt
)
from PySide.QtGui import (
        QDesktopWidget,
        QApplication
)

class Composer(QObject):

    def compose(self, widgetsByLayout, centralLayout = None):
        """Compose widget(s) into layout(s)"""
        for layout, widgets in widgetsByLayout.items():
            for widget in widgets:
                # Add widget to layout
                layout.addWidget(widget)
                # Either set this layout as central, or add it to central layout
                centralLayout.addLayout(layout) if(centralLayout) \
                        else self.setLayout(layout)

        if(centralLayout):
            self.setLayout(centralLayout)


    def widgetize(self, title = 'Widget'):
        """Widgetize main window and set title"""
        #self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowTitle(title)

    def position(self):
        """By default, position on top, centered"""
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() - self.frameSize().width()) / 2,
                  resolution.height() - self.frameSize().height() / 2)
        #self.move(QApplication.desktop().screen().rect().center()
                #- self.rect().center())

    def scale(self):
        """Scale widget to screen"""
        resolution = QDesktopWidget().screenGeometry()
        self.resize(resolution.width() / 2, resolution.height() / 6)



