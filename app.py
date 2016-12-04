#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

from ui_manager import *

if __name__ == "__main__":
    app = QtGui.QApplication(['BestFit Algorithm'])
    window = BestfitApp()
    window.show()
    app.exec_()
