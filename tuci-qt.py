#!/usr/bin/env python
# coding=utf-8

import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtWebKit


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")
        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        #self.showFullScreen()
        layout = QHBoxLayout()
        self.text = QTextEdit()
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        #layout.addWidget(self.text)
        layout.addWidget(self.view)
        #textItem = QGraphicsTextItem('test')
        #textItem.linkHovered.connect(self.itemHover)
        anotherItem = QGraphicsTextItem()
        anotherItem.setHtml('<html><style>a { color: green; text-decoration: none; } a:hover { color: red; }</style><body>Another one <a id="test"  href="test">bites!</a></body></html>')
        anotherItem.linkHovered.connect(self.itemHover)
        anotherItem.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        #self.scene.addItem(textItem)
        self.scene.addItem(anotherItem)


        # USE THIS
        textBrowser = QtWebKit.QWebView()
        webPage = QtWebKit.QWebPage()
        webPage.mainFrame().setHtml('<html><style>a { color: green; text-decoration: none; } a:hover { color: red; }</style><body>Another one <a id="test"  href="test">bites!</a></body></html>')
        webPage.linkHovered.connect(self.itemHover)
        textBrowser.setPage(webPage)
        layout.addWidget(textBrowser)
        # END OF THIS


        label = QLabel('<html><style>a { color: green; text-decoration: none; }</style><body>Another one <a id="test"  href="test">bites!</a></body></html>')
        label.linkHovered.connect(self.itemHover)
        label.setStyleSheet('''a {
                            color: white;
                            }''')
        layout.addWidget(label)
        # Set dialog layout
        self.setLayout(layout)

    def itemHover(self, item):
        print item


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
