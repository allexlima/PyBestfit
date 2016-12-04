#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

import random

""" List of some MIPS registers available for programs usage """
REGISTERS = ['r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15']

""" List of basic process states, for single-task systems """
P_STATES = ['waiting', 'running', 'done']

TESTING = False
SIZES = [10, 20, 30, 40]

ERRORS = []


def g_int_value(ab=None):
    val = None
    if not ab:
        val = int(random.random() * 100) + 1
    elif isinstance(ab, tuple):
        val = random.randint(ab[0], ab[1])
    return val


def g_list_value(array):
    if isinstance(array, list):
        random.shuffle(array)
        aux = random.randint(0, len(array)-1)
        return array[aux]
    else:
        pass
