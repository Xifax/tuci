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

        # Sentence view
        self.view, self.page = QWebView(), QWebPage()
        self.view.setPage(self.page)
        # TODO: update dynamically on parent widget resize events (somehow?)
        self.view.setMinimumSize(parent.width(), parent.height() / 2)

        # Info view
        self.infoView, self.infoPage = QWebView(), QWebPage()
        self.infoView.setPage(self.infoPage)
        self.infoView.setMaximumSize(parent.width() / 2, parent.height())

        # Active terms and sentence
        self.terms, self.example = {}, u''
        # Default style
        self.css = 'solarized-light'

        # Composition
        self.compose({
            QHBoxLayout(): [self.infoView, self.view]
        })

        # Initialize events
        self.page.linkHovered.connect(self.showInfo)
        self.page.setLinkDelegationPolicy(QWebPage.DelegateExternalLinks)
        self.page.linkClicked.connect(self.queryServer)

        # Initialize style
        self.clearPages()

    def update(self, sentence, terms):
        """Update page contents"""
        # 0. Process and style translated terms
        html = self.style(self.process(sentence, terms))
        # 2. Update page
        self.page.mainFrame().setHtml(html)

    def process(self, sentence, terms):
        """Prepare html body based on translations"""
        self.terms, self.example = terms, sentence
        text = unicode(sentence)
        template = '<a href="%s">%s</a>'
        # Compose sentence
        # TODO: differentiate colors, if two or more terms are side by side
        for term in terms:
            text = text.replace(term, template % (term, term))
        return text

    def style(self, body, style = 'solarized-light'):
        """Style html body"""
        # see: https://github.com/thomasf/solarized-css
        # TODO: read from css files based on style
        # TODO: allow user to pick fonts
        # TODO: allow for dynamic font-size
        return '''
        <html>
            <style>
                body {
                    font-size: 1.5em;
                    font-family: 'A-OTF MainichiNewspapersM Pro L';
                }
                a {
                    color: #b58900;
                    text-decoration: none;
                }
                a:hover { color: #cb4b16; }
                a:visited { color: #cb4b16; }
                html {
                    background-color: #fdf6e3;
                    color: #657b83;
                    margin: 1em;
                }
            </style>
            <body>
                %s
            </body>
        </html>
        ''' % body

    def clearPages(self):
        """Reset pages"""
        self.page.mainFrame().setHtml(self.style(''))
        self.infoPage.mainFrame().setHtml(self.style(''))

    def showInfo(self, item):
        """Update terms info"""
        # TODO: style translation separately (add <strong> and colors)!
        html = self.style(self.terms.get(item, ''))
        self.infoPage.mainFrame().setHtml(html)

    def queryServer(self, item):
        """Query SRS server"""
        # TODO: implement
        print item.toString(), self.example
