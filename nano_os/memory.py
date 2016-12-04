#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

import support


class Block(object):
    def __init__(self, size=None):
        self.address = None
        self.size = {
            'total': size,
            'available': size
        }
        self.content = []
        self.__pseudo_values_maker()

    def __pseudo_values_maker(self):
        self.address = hex(support.g_int_value((10000, 30000)))

        if support.TESTING is not True:
            m_size = support.g_int_value()
            self.size.update({
                'total': m_size,
                'available': m_size
            })


class Memory(object):
    def __init__(self, width):
        self.__list = []
        self.width = width
        self.__pseudo_values_maker()

    def __pseudo_values_maker(self):
        for i in range(0, self.width, 1):
            if support.TESTING is True:
                self.__list.append(Block(support.SIZES[i]))
            else:
                self.__list.append(Block())

    def get_block(self, address):
        try:
            return next(item for item in self.__list if item.address == address)
        except StopIteration:
            pass

    def get_array(self):
        return self.__list

    def alloc_in(self, obj, address):
        try:
            block = self.get_block(address)
            block.content.append(obj)
            block.size.update({
                'available': block.size['total'] - obj.size
            })
            obj.state = support.P_STATES[1]
        except AttributeError:
            pass


class MemoryManager(Memory):
    def __init__(self, m_blocks_quantity=10):
        super(MemoryManager, self).__init__(m_blocks_quantity if support.TESTING is not True else len(support.SIZES))
        self.memory = self.get_array()

    @staticmethod
    def __listing_style(obj):
        return {
            'address': obj.address,
            'size': {
                'total': "{0} KiB".format(obj.size['total']),
                'available': "{0} KiB".format(obj.size['available']),
            },
            'content': [{'pid': item.pid, 'size': '{0} KiB'.format(item.size)} for item in obj.content]
        }

    def binary_search(self, value, vector):
        middle = int(len(vector)/2)

        if len(vector) == 2:
            return vector
        elif value > vector[middle]:
            return self.binary_search(value, vector[middle:])
        elif value < vector[middle]:
            return self.binary_search(value, vector[:middle+1])

    def best_fit(self, process):
        process_size = process.size
        distance = 1000
        best_position = None

        for i in range(0, len(self.memory)):
            block_size = self.memory[i].size['available']
            if abs(block_size - process_size) < distance and block_size >= process_size:
                best_position = i
                distance = abs(block_size - process_size)

        if best_position is not None:
            return self.memory[best_position].address
        else:
            support.ERRORS.append("[Warning] Could not find an available space for process {0}.".format(process.pid))

    def alloc(self, obj):
        address = self.best_fit(obj)
        if address is not None:
            self.alloc_in(obj, address)
            return address
        else:
            pass

    def free(self, address):
        self.get_block(address)

    def show(self, address=None):
        aux = None

        if address:
            try:
                aux = MemoryManager.__listing_style(self.get_block(address))
            except AttributeError:
                pass
        else:
            aux = []
            for item in range(0, len(self.memory), 1):
                aux.append(MemoryManager.__listing_style(self.memory[item]))

        return aux
