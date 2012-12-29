#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    QT layouts and widgets composer
"""

# external #
from PySide.QtCore import QObject

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


    def style(self):
        pass

    def position(self):
        pass


