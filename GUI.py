#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:52:37 2018

@author: okur
"""

import sys
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QMainWindow, QAction, qApp, QVBoxLayout, QFrame, QSplitter,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class appWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.startMenu()
        self.showWindow()
    
    def showWindow(self):
        self.setWindowTitle('Histogram Matching')    
        self.showMaximized()
        
        
    def startMenu(self):
        quitBar = QAction('Exit', self) 
        quitBar.setShortcut('Ctrl+Q')
        quitBar.setStatusTip('Exit application')
        quitBar.triggered.connect(qApp.quit)
        
        inputBar = QAction('Open Input', self)
        inputBar.setStatusTip('Open Input Image')
        
        targetBar = QAction('Open Target', self)
        targetBar.setStatusTip('Open Target Image')

        equalizeButton = QAction('Equalize Histogram', self)
        equalizeButton.triggered.connect(self.equalizeHistogram)
        equalizeButton.setStatusTip('Equalize Histogram')
        
        self.statusBar()
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(equalizeButton)
        appMenuBar = self.menuBar()
        appMenu = appMenuBar.addMenu('File')
        appMenu.addAction(inputBar)
        appMenu.addAction(targetBar)
        appMenu.addAction(quitBar)
        
        widget = QWidget()
        self.setWidget(widget)
        self.setCentralWidget(widget)
        
    def equalizeHistogram(self):
        print('abdullah')
    
    
    def setWidget(self, widget):     
        widgetLayout = QVBoxLayout(widget)
        
        frame1 = QFrame(widget)
        frame1.setFrameShape(QFrame.StyledPanel)
        
        label1 = QLabel(widget)
        label1.setText('Input')
        
        frame2 = QFrame(widget)
        frame2.setFrameShape(QFrame.StyledPanel)

        label2 = QLabel(widget)
        label2.setText('Target')
        
        frame3 = QFrame(widget)
        frame3.setFrameShape(QFrame.StyledPanel)
        
        label3 = QLabel(widget)
        label3.setText('Result')
        
        widgetLayout.addWidget(label1)
        widgetLayout.addWidget(label2)
        widgetLayout.addWidget(label3)
        widgetLayout.addWidget(frame1)
        widgetLayout.addWidget(frame2)
        widgetLayout.addWidget(frame3)
        widget.setLayout(widgetLayout)

app = QApplication(sys.argv)
application = appWindow()
sys.exit(app.exec_())


