#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

import support


class Process(object):
    def __init__(self, name, user):
        self.pid = None
        self.name = name
        self.context = {}
        self.memory = []
        self.user = user
        self.priority = None
        self.size = None
        self.start_time = None
        self.pseudo_values_maker()

    def pseudo_values_maker(self):
        """
        In this method, I'll generate the values for process attributes.
        The majority of the values are sorted pseudo-randomly by g_int_value([ab]) function,
        in m_manage/support.py.
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
        """
        self.size = support.g_int_value()

        # Creates context info
        for i in range(support.g_int_value((2, 10))):
            self.context.update({
                support.g_list_value(support.REGISTERS): support.g_int_value()
            })


class Memory(object):
    pass
