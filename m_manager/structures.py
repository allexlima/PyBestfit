#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

import datetime
import support


class Process(object):
    def __init__(self, name, user):
        self.pid = None
        self.name = name
        self.context = {}
        self.memory_addresses = []
        self.user = user
        self.priority = None
        self.size = None
        self.start_time = None
        self.state = None
        self.pseudo_values_maker()

    def pseudo_values_maker(self):
        """
        In this method, I'll generate the values for process attributes.
        The majority of the values are sorted pseudo-randomly by g_int_value([ab]) function,
        in m_manage/support.py.
        :return void
        """

        """
        Generate PID number
        """
        self.pid = support.g_int_value()

        """
        Like all UNIX systems, according with Maziero (2013, 2.5.5, p. 56),
        -20 means less priority while +19 means more priority in process.
        """
        self.priority = support.g_int_value((-20, 19))

        """
        The process size here follows the computational bits metrics units, according
        Tanenbaum, A. S., & Zucchi, W. L. (2009) and also ISO/IEC 80000.
        By default in this code, I'll use kibibytes as measure unit, i.e. KiB, for the process sizes.
        So, process size = object.size [attribute is an integer value] + KiB [abstract/convention measure unit]
        """
        self.size = support.g_int_value()

        """
        Update context attribute [it's a dict structure] with {register: 0xVALUE}.
        Registers names were based in MIPS registers and are listed in REGISTERS, in m_manage/support.py.
        """
        for i in range(0, support.g_int_value((2, 10)), 1):
            self.context.update({
                support.g_list_value(support.REGISTERS): hex(support.g_int_value())
            })

        """
        Get current date and time to attach in start_time attribute in ISO format
        """
        self.start_time = datetime.datetime.now().isoformat()

        """
        Set by default state 'waiting' for the process
        """
        self.state = support.P_STATES[0]


class ProcessManager(object):
    def __init__(self):
        self.__list = []

    def create(self, nome, user):
        """
        This method allow the process object creation and put that object in the ProcessList
        :param nome: Process name
        :param user: Process owner
        :return: void
        """

        obj = Process(nome, user)
        self.__insert(obj)
        return obj.pid

    def __insert(self, process):
        """
        This 'private' method will insert the object process in a Process list through the append list function
        :param process:
        :return:
        """
        self.__list.append(process)

    def get(self, pid):
        """
        This method will return the object of process through PID informed

        :param pid: Might contains the process' ID, an integer value
        :return: The process object
        :rtype object
        """
        try:
            return next(item for item in self.__list if item.pid == pid)
        except StopIteration:
            pass

    @staticmethod
    def __listing_style(obj):
        """
        This static method is where can be defined the return process style
        :param obj: Process object
        :return: Listing of process values
        :rtype dict
        """
        return {
            'pid': obj.pid,
            'name': obj.name,
            'user': obj.user,
            'priority': obj.priority,
            'state': obj.state,
            'size': "{0} KiB".format(obj.size),
            'start_time': obj.start_time,
            'context': obj.context,
            'memory_addresses': obj.memory_addresses
        }

    def show(self, pid=None):
        """
        This method will show a dictionary with all process' values when it's called
        If is passed the PID parameter, the method will return just info about this process' PID
        else, a list of dict within all process in a ProcessList will be returned
        :rtype dict or list
        """
        aux = None

        if pid:
            try:
                aux = ProcessManager.__listing_style(self.get(pid))
            except AttributeError:
                pass
        else:
            aux = []
            for item in range(0, len(self.__list), 1):
                aux.append(ProcessManager.__listing_style(self.__list[item]))

        return aux

    def kill(self, pid):
        """
        This method will delete the process' object, through PID informed, from
        the __list attribute list.

        :param pid: Might contains the process' ID (PID), an integer value
        :return: void
        """
        self.__list[:] = [item for item in self.__list if item.pid != pid]


class Block(object):
    def __init__(self):
        self.address = None
        self.size = {
            'total': None,
            'available': None
        }
        self.content = []
        self.pseudo_values_maker()

    def pseudo_values_maker(self):
        self.address = hex(support.g_int_value((10000, 30000)))
        m_size = support.g_int_value()
        self.size.update({
            'total': m_size,
            'available': m_size
        })


class Memory(object):
    def __init__(self, width=10):
        self.__list = []
        self.width = width
        self.pseudo_values_maker()

    def get(self, address):
        try:
            return next(item for item in self.__list if item.address == address)
        except StopIteration:
            pass

    @staticmethod
    def __listing_style(obj):
        return {
            'address': obj.address,
            'size': {
                'total': "{0} KiB".format(obj.size['total']),
                'available': "{0} KiB".format(obj.size['available']),
            },
            'content': obj.content
        }

    def show(self, address=None):
        aux = None

        if address:
            try:
                aux = Memory.__listing_style(self.get(address))
            except AttributeError:
                pass
        else:
            aux = []
            for item in range(0, len(self.__list), 1):
                aux.append(Memory.__listing_style(self.__list[item]))

        return aux

    def pseudo_values_maker(self):
        for i in range(0, self.width, 1):
            self.__list.append(Block())
