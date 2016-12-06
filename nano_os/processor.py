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
        self.user = user
        self.priority = None
        self.size = None
        self.start_time = None
        self.state = None
        self.__pseudo_values_maker()

    def __pseudo_values_maker(self):
        self.pid = support.g_int_value()

        self.priority = support.g_int_value((-20, 19))

        self.size = support.g_int_value()
        if support.TESTING is True:
            self.size = support.g_int_value((support.SIZES[0], support.SIZES[-1]))

        for i in range(0, support.g_int_value((2, 10)), 1):
            self.context.update({
                support.g_list_value(support.REGISTERS): hex(support.g_int_value())
            })

        self.start_time = datetime.datetime.now().isoformat()
        self.state = support.P_STATES[0]


class ProcessManager(object):
    def __init__(self):
        self.__list = []

    @staticmethod
    def __listing_style(obj):
        return {
            'pid': obj.pid,
            'name': obj.name,
            'user': obj.user,
            'priority': obj.priority,
            'state': obj.state,
            'size': "{0} KiB".format(obj.size),
            'start_time': obj.start_time,
            'context': obj.context,
        } if support.TESTING is not True else {'pid': obj.pid, 'size': "{0} KiB".format(obj.size)}

    def __insert(self, process):
        self.__list.append(process)

    def create(self, nome, user):
        obj = Process(nome, user)
        self.__insert(obj)
        return obj.pid

    def get(self, pid):
        try:
            return next(item for item in self.__list if item.pid == pid)
        except StopIteration:
            pass

    def show(self, pid=None):
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
        self.__list[:] = [item for item in self.__list if item.pid != pid]

