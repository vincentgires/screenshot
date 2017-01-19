#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class ImageLabel(QtWidgets.QLabel):
    
    def __init__(self, parent=None):
        super().__init__()
        self.origin = QtCore.QPoint()
        self.rubber_band = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle, self)
        
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.origin = QtCore.QPoint(event.pos())
            self.rubber_band.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
            self.rubber_band.show()

    def mouseMoveEvent(self, event):
        if not self.origin.isNull():
            self.rubber_band.setGeometry(
                QtCore.QRect(self.origin, event.pos()).normalized())

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.rubber_band.hide()

class AreaWindow(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        #self.setWindowTitle('Screenshot')
        geometry = app.desktop().availableGeometry()
        self.setFixedSize(geometry.width(), geometry.height())
        #self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowFullScreen)
        self.showFullScreen()
        
        screen = QtWidgets.QApplication.primaryScreen()
        pixmap = screen.grabWindow(0)
        label = ImageLabel(self)
        label.setPixmap(pixmap)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(label)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.show()
        
        
if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    window = AreaWindow()
    sys.exit(app.exec_())
