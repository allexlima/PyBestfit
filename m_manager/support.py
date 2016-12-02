#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

REGISTERS = []


def g_int_value():
    return int(random.random() * 100)


def g_register_name():
    random.shuffle(REGISTERS)
    aux = random.randint(0, len(REGISTERS)-1)
    return REGISTERS[aux]
