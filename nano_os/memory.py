#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

import support


class Block(object):
    def __init__(self):
        self.address = None
        self.size = {
            'total': None,
            'available': None
        }
        self.content = []
        self.__pseudo_values_maker()

    def __pseudo_values_maker(self):
        self.address = hex(support.g_int_value((10000, 30000)))
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
            self.__list.append(Block())

    def get_block(self, address):
        try:
            return next(item for item in self.__list if item.address == address)
        except StopIteration:
            pass

    def get_array(self):
        return self.__list

    def alloc_in(self, obj, address):
        block = self.get_block(address)
        block.content.append(obj)


class MemoryManager(Memory):
    def __init__(self, m_blocks_quantity=10):
        super(MemoryManager, self).__init__(m_blocks_quantity)

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

    def __best_fit(self, process_size):
        pass

    def alloc(self, obj):
        pass

    def free(self, address):
        pass

    def show(self, address=None):
        aux = None

        if address:
            try:
                aux = MemoryManager.__listing_style(self.get(address))
            except AttributeError:
                pass
        else:
            aux = []
            for item in range(0, len(self.__list), 1):
                aux.append(MemoryManager.__listing_style(self.__list[item]))

        return aux
