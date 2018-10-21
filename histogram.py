#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 13:09:52 2018

@author: okur
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QSizePolicy

def read_image(path):
    imageBGR = cv2.imread(path, 1)
    image = cv2.cvtColor(imageBGR, cv2.COLOR_BGR2RGB)
    return image


def calculate_histogram(image):
    p1,p2,p3 = image.shape
    histogram = np.zeros([256, p3], np.int16)
    for i in range(p1):
        for j in range(p2):
            for z in range(p3):
                intensity = image[i,j,z]
                histogram[intensity, z] += 1 
    return histogram

class PlotCanvas(FigureCanvas):
    def __init__(self, histogram, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(311)
 
        FigureCanvas.__init__(self, fig)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plotHistogram(histogram)

    def plotHistogram(self, histogram):
        x = range(256)
        plt1, plt2, plt3 = self.figure.add_subplot(311)
        plotHistogram.bar(x, histogram[:,0],color='r' )
        plotHistogram1.bar(x, histogram[:,1],color='g' )
        plotHistogram2.bar(x, histogram[:,2],color='b' )
        self.draw()
        
        
path = 'color1.png'
image = read_image(path)
histogram = calculate_histogram(image)
#canvas = PlotCanvas(histogram)
x = range(256)
a,b,c = plt.subplot(3,1)
a.bar(x, histogram[:,0],color='r' )
b.bar(x, histogram[:,1],color='g' )
c.bar(x, histogram[:,2],color='b' )
plt.show()

