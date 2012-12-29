#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copied & analyzed text
"""

# external #
from PySide.QtGui import (
        QWidget,
        QHBoxLayout,
)
from PySide.QtWebKit import (
        QWebView,
        QWebPage,
)

# own #
from composer import Composer

class Text(QWidget, Composer):

    def __init__(self, parent=None):
        super(Text, self).__init__(parent)

        # Web view
        self.view, self.page = QWebView(), QWebPage()
        self.view.setPage(self.page)

        # Composition
        self.compose({
            QHBoxLayout(): [self.view]
        })

        # Initialize events
        self.page.linkHovered.connect(self.info)

        # Initialize style

    def update(self, html):
        """Update page contents"""
        # 1. Style contents
        # 2. Update page
        self.page.mainFrame().setHtml(html)

    def style(self, text):
        pass

    def info(self, item):
        pass

