#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com


from PyQt4 import QtGui, QtCore
import interface
import webbrowser
import nano_os as myos
import nano_os.support as log_error
import operator


class MyTableModel(QtCore.QAbstractTableModel):

    def __init__(self, parent, my_list, header, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.my_list = my_list
        self.header = header

    def rowCount(self, parent):
        return len(self.my_list)

    def columnCount(self, parent):
        return len(self.my_list[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole:
            return None
        return self.my_list[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]
        return None

    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
        self.my_list = sorted(self.my_list,
                              key=operator.itemgetter(col))
        if order == QtCore.Qt.DescendingOrder:
            self.my_list.reverse()
        self.emit(QtCore.SIGNAL("layoutChanged()"))


class BestfitApp(QtGui.QMainWindow, interface.Ui_BestFit):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.menuAjudar.addAction(self.actionTeam.triggered.connect(self.about))
        self.menuAjudar.addAction(self.actionGithub.triggered.connect(self.github))
        self.logs_manager()
        self.memoryAlloc.clicked.connect(self.button_alloc)
        self.updateInfo.clicked.connect(self.button_update)
        self.updateInfo.setText("Create Values")
        self.memory_m = None
        self.process_m = myos.ProcessManager()
        self.p = None
        self.memoryAlloc.setDisabled(True)

    def alert(self, text, title="Alert", code=2):
        message = QtGui.QMessageBox(self)
        message.setIcon(code)
        message.setText(unicode(text))
        message.setWindowTitle(title)
        message.setWindowModality(QtCore.Qt.ApplicationModal)
        message.exec_()

    def about(self):
        self.alert(
            u"\nTrabalho desenvolvido para compor a nota parcial da 3ª ARE da disciplina de " +
            u"Sistemas Operacionais, ministrada pelo Prof.ª M.Sc. Ângela Lima. " +
            u"\n\nDesenvolvido por: Allex Lima, Daniel Bispo, Paulo Moraes e Renan Barroncas",
            title="Sobre",
            code=1
        )

    def logs_manager(self, reset=None):
        if reset is not None:
            myos.ERRORS = []
            log_error.ERRORS = []

        myos.ERRORS += log_error.ERRORS

        if not len(myos.ERRORS):
            self.logView.setText("No log registers")
        else:
            log = ""
            for i in range(len(myos.ERRORS)):
                log += myos.ERRORS[i] + "\n"
            self.logView.setText(log)

    def memory_manager_table(self, contents, header):
        self.tableMemory.setModel(MyTableModel(self, contents, header))
        self.tableMemory.setSortingEnabled(True)

    def processes_manager_table(self, contents, header):
        self.tableProcess.setModel(MyTableModel(self, contents, header))
        self.tableProcess.setSortingEnabled(True)

    def button_alloc(self):
        for i in range(0, len(self.p), 1):
            self.memory_m.alloc(self.process_m.get(self.p[i]))

        myos.ERRORS.append("\n--- [allocating] ---\n")
        self.__inflate_memory_table()
        self.__inflate_process_table()
        self.memoryAlloc.setDisabled(True)
        myos.ERRORS.append("[Done] Allocation done successfully")
        self.logs_manager()

    def __inflate_memory_table(self):
        self.tableMemory.reset()
        t_m_header = ["Address", "Total Size", "Available Size", "Content"]
        t_m_contents = []

        for item in range(0, len(self.memory_m.memory), 1):
            block = self.memory_m.memory[item]

            t_m_contents.append((block.address, '{0} KiB'.format(block.size['total']), '{0} KiB'.format(block.size['available']),
                                str(["{0}:{1} KiB".format(process.pid, process.size) for process in block.content])))

        if len(t_m_contents):
            myos.ERRORS.append("[Info] Creating memory table")
            self.memory_manager_table(t_m_contents, t_m_header)
        else:
            myos.ERRORS.append("[Error] Could not create Process and Memory tables.")

    def __inflate_process_table(self):
        t_p_header = ["PID", "Size", "Name", "User", "Priority", "State", "Start", "Context"]
        t_p_contents = []

        for item in range(0, len(self.p), 1):
            process = self.process_m.get(self.p[item])
            t_p_contents.append(
                (process.pid, '{0} KiB'.format(process.size), process.name, process.user, process.priority,
                 process.state, process.start_time, str(process.context)))

        if len(t_p_contents):
            myos.ERRORS.append("[Info] Creating process table")
            self.processes_manager_table(t_p_contents, t_p_header)
        else:
            myos.ERRORS.append("[Error] Could not create Process table.")

    def button_update(self):
        self.updateInfo.setText("Update")
        self.tableProcess.reset()
        self.memoryAlloc.setDisabled(False)

        self.logs_manager(True)

        myos.TESTING = True if self.randomCheck.isChecked() else False
        myos.ERRORS.append(
            "[Info] Test mode is {0}".format(
                'on. Using programmed values.' if myos.TESTING is True else 'off. Using pseudo-randomly sizes values.')
        )

        self.memory_m = myos.MemoryManager()
        self.process_m = myos.ProcessManager()

        self.p = [
            self.process_m.create("iam_using.cpp", "allex"),
            self.process_m.create("coding_in.py", "daniel"),
            self.process_m.create("loving.js", "paulo"),
            self.process_m.create("wanna_learn.lua", "renan")
        ]

        myos.ERRORS.append("[Info] Process with PID {0}, {1}, {2} and {3} were created.".format(self.p[0], self.p[1], self.p[2], self.p[3]))

        self.__inflate_memory_table()
        self.__inflate_process_table()
        self.logs_manager()

    @staticmethod
    def github():
        webbrowser.open("https://github.com/allexlima/PyBestfit")
