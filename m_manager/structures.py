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
        By default in this code, I'll use mebi-bytes as measure unit, i.e. MiB, for the process sizes.
        So, process size = object.size [attribute is an integer value] + MiB [abstract/convention measure unit]
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
        obj = Process(nome, user)
        self.__insert(obj)
        return obj.pid

    def __insert(self, process):
        self.__list.append(process)

    def get(self, pid):
        """
        This method will return the object of process through PID informed

        :param pid: Might contains the process' ID, an integer value
        :return: The process object
        :rtype object
        """
        return [item for item in self.__list if item.pid == pid][0]

    @staticmethod
    def __listing_style(obj):
        return {
            'pid': obj.pid,
            'name': obj.name,
            'user': obj.user,
            'priority': obj.priority,
            'size': "{0} MiB".format(obj.size),
            'start_time': obj.start_time,
            'context': obj.context,
            'memory_addresses': obj.memory_addresses
        }

    def show(self, pid=None):
        """
        This method will show a dictionary with all process' values when it's called
        :rtype dict
        """
        aux = None

        if pid:
            aux = ProcessManager.__listing_style(self.get(pid))
        else:
            aux = []
            for item in range(0, len(self.__list), 1):
                aux.append(ProcessManager.__listing_style(self.__list[item]))

        return aux

    def delete(self, pid):
        """
        This method will delete the process' object, through PID informed, from
        the __list attribute list.

        :param pid: Might contains the process' ID (PID), an integer value
        :return: void
        """
        self.__list[:] = [item for item in self.__list if item.pid != pid]


class Memory(object):
    pass

