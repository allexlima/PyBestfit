# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BestFit(object):
    def setupUi(self, BestFit):
        BestFit.setObjectName(_fromUtf8("BestFit"))
        BestFit.resize(800, 500)
        BestFit.setMinimumSize(QtCore.QSize(800, 500))
        BestFit.setMaximumSize(QtCore.QSize(800, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BestFit.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(BestFit)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.memoryAlloc = QtGui.QPushButton(self.centralwidget)
        self.memoryAlloc.setGeometry(QtCore.QRect(637, 420, 131, 41))
        self.memoryAlloc.setObjectName(_fromUtf8("memoryAlloc"))
        self.randomCheck = QtGui.QCheckBox(self.centralwidget)
        self.randomCheck.setGeometry(QtCore.QRect(350, 420, 141, 41))
        self.randomCheck.setObjectName(_fromUtf8("randomCheck"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 751, 391))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.processTab = QtGui.QWidget()
        self.processTab.setObjectName(_fromUtf8("processTab"))
        self.tableMemory = QtGui.QTableView(self.processTab)
        self.tableMemory.setGeometry(QtCore.QRect(0, 0, 749, 355))
        self.tableMemory.setObjectName(_fromUtf8("tableMemory"))
        self.tabWidget.addTab(self.processTab, _fromUtf8(""))
        self.memoryTab = QtGui.QWidget()
        self.memoryTab.setAccessibleName(_fromUtf8(""))
        self.memoryTab.setObjectName(_fromUtf8("memoryTab"))
        self.tableProcess = QtGui.QTableView(self.memoryTab)
        self.tableProcess.setGeometry(QtCore.QRect(0, 0, 749, 355))
        self.tableProcess.setObjectName(_fromUtf8("tableProcess"))
        self.tabWidget.addTab(self.memoryTab, _fromUtf8(""))
        self.logTab = QtGui.QWidget()
        self.logTab.setObjectName(_fromUtf8("logTab"))
        self.logView = QtGui.QTextEdit(self.logTab)
        self.logView.setEnabled(True)
        self.logView.setGeometry(QtCore.QRect(0, 0, 761, 361))
        self.logView.setAutoFormatting(QtGui.QTextEdit.AutoAll)
        self.logView.setReadOnly(True)
        self.logView.setTabStopWidth(20)
        self.logView.setObjectName(_fromUtf8("logView"))
        self.tabWidget.addTab(self.logTab, _fromUtf8(""))
        self.updateInfo = QtGui.QPushButton(self.centralwidget)
        self.updateInfo.setGeometry(QtCore.QRect(497, 420, 131, 41))
        self.updateInfo.setObjectName(_fromUtf8("updateInfo"))
        BestFit.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(BestFit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAjudar = QtGui.QMenu(self.menubar)
        self.menuAjudar.setSeparatorsCollapsible(True)
        self.menuAjudar.setObjectName(_fromUtf8("menuAjudar"))
        BestFit.setMenuBar(self.menubar)
        self.actionGithub = QtGui.QAction(BestFit)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("img/github.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGithub.setIcon(icon1)
        self.actionGithub.setIconVisibleInMenu(True)
        self.actionGithub.setObjectName(_fromUtf8("actionGithub"))
        self.actionTeam = QtGui.QAction(BestFit)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("img/about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTeam.setIcon(icon2)
        self.actionTeam.setIconVisibleInMenu(True)
        self.actionTeam.setObjectName(_fromUtf8("actionTeam"))
        self.menuAjudar.addAction(self.actionGithub)
        self.menuAjudar.addAction(self.actionTeam)
        self.menubar.addAction(self.menuAjudar.menuAction())

        self.retranslateUi(BestFit)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BestFit)

    def retranslateUi(self, BestFit):
        BestFit.setWindowTitle(_translate("BestFit", "Bestfit Memory Allocation Algorithm", None))
        self.memoryAlloc.setText(_translate("BestFit", "Memory Alloc", None))
        self.randomCheck.setText(_translate("BestFit", "Testing mode", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.processTab), _translate("BestFit", "Memory", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.memoryTab), _translate("BestFit", "Processes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.logTab), _translate("BestFit", "Logs", None))
        self.updateInfo.setText(_translate("BestFit", "Update", None))
        self.menuAjudar.setTitle(_translate("BestFit", "More", None))
        self.actionGithub.setText(_translate("BestFit", "Github", None))
        self.actionTeam.setText(_translate("BestFit", "About", None))

