#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:52:37 2018
@author: okur
"""

import histogram
import sys
from PyQt5.QtWidgets import ( QLabel, QApplication, QWidget, QMainWindow, QAction, qApp,
    QVBoxLayout, QFrame, QFileDialog, QHBoxLayout, QGroupBox, QGridLayout, QDesktopWidget)
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
        self.inputImage = inputBar.triggered.connect(self.openInputImage)
        
        targetBar = QAction('Open Target', self)
        targetBar.setStatusTip('Open Target Image')
        self.targetImage = targetBar.triggered.connect(self.openTargetImage)
        
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
    
    def openInputImage(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        image = histogram.read_image(imagePath)
        histogram_input = histogram.calculate_histogram(image)
        title = 'input image'
        histogram.plot_histogram(histogram_input, title)

    
    def openTargetImage(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        image = histogram.read_image(imagePath)
        histogram_output = histogram.calculate_histogram(image)
        title = 'target image'
        histogram.plot_histogram(histogram_output, title)
        
    def equalizeHistogram(self):
        print('...')
   
    def setWidget(self, widget):     
        widgetLayout = QGridLayout(widget)
        
        box1 = QGroupBox(widget)
        box1.setTitle('Input')
        
        vbox1 = QVBoxLayout(box1)
        label11 = QLabel()
        label12 = QLabel()
        vbox1.addWidget(label11)
        vbox1.addWidget(label12)
        vbox1.addStretch()
        box1.setLayout(vbox1)
        
        box2 = QGroupBox(widget)
        box2.setTitle('Output')
        
        vbox2 = QVBoxLayout(box2)
        label21 = QLabel()
        label22 = QLabel()
        vbox2.addWidget(label21)
        vbox2.addWidget(label22)
        vbox2.addStretch()
        box2.setLayout(vbox2)
        
        
        box3 = QGroupBox(widget)
        box3.setTitle('Result')
        vbox3 = QVBoxLayout(box3)
        label31 = QLabel()
        label32 = QLabel()
        vbox3.addWidget(label31)
        vbox3.addWidget(label32)
        vbox3.addStretch()
        box3.setLayout(vbox3)
        
        widgetLayout.addWidget(box1,0,0)
        widgetLayout.addWidget(box2,0,1)
        widgetLayout.addWidget(box3,0,2)
        widget.setLayout(widgetLayout)
        widget.show()
        
app = QApplication(sys.argv)
application = appWindow()
sys.exit(app.exec_())
