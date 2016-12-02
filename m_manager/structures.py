#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


class Process(object):
    def __init__(self):
        self.pid = None
        self.context = {}
        self.memory = []
        self.user = None
        self.priority = None
        self.size = None
        self.start_time = None

    def pseudo_values_maker(self):
        pass

class Memory(object):
    pass
