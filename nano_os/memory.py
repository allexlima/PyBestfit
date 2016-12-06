#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

import support
from threading import Thread


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
        """
        In this method, I'll generate the values for Block attributes.
        The majority of the values are sorted pseudo-randomly by g_int_value([ab]) function,
        in nano_os/support.py.
        :return void
        """

        """
        Block address is an random int between 10000 and 30000 converted to hexadecimal
        """
        self.address = hex(support.g_int_value((10000, 30000)))

        """
        If Testing mode is off, create more random values for block size
        """
        if support.TESTING is not True:
            """
            Get an random int for m_size var then attach this value in attribute size, that is a dict structure
            with 'total' and 'available' info about block size
            """
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
        """
        In this method, I'll insert Block objects in self.__list list attribute
        :return void
        """

        for i in range(0, self.width, 1):
            if support.TESTING is True:
                """
                If Testing mode is On, then put blocks with sizes from support.SIZES list,
                available in nano_os/support.py
                """
                self.__list.append(Block(support.SIZES[i]))
            else:
                """
                Else, blocks will have random value sizes
                """
                self.__list.append(Block())

    def get_block(self, address):
        """
        This method will return an block Object by address attribute of this one.
        :param address: string with address block value
        :return: Block Object
        """
        try:
            return next(item for item in self.__list if item.address == address)
        except StopIteration:
            pass

    def get_array(self):
        """
        Return the list of blocks, i.e. Memory Array
        :return: list
        """
        return self.__list

    def alloc_in(self, obj, address):
        """
        This method will alloc some obj (Process Object) in a particular memory block
        through the address (Block address attribute) of this one.

        :param obj: must be a Process Object
        :param address: must be a address attribute from some Block Object
        :return: void
        """
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

    def best_fit(self, process):
        """
        This is the MAIN method, since now, of this project.
        It'll return the best block to allocate some process, using as an parameter the process size.
        Basically, it will return a block with size more close of the process size.

            Block.size <= best_position (for the process size) <= Block.size

        :param process: must be an Process Object
        :return: an Address attribute from the best Block to allocate this Process Object
        """

        """
        Get the process size
        """
        process_size = process.size

        """
        Set an arbitrary initial value to distante.
        This var will be used to discover HOW DISTANT last block was from that actual block, in loop
        """
        distance = 1000

        """
        Set initially best_position as None
        because the algorithm can not find some Block with available size to allocate it one
        """
        best_position = None

        """
        This loop will check block per block from the memory analysing the Block and Process size
        to find the best position
        """
        for i in range(0, len(self.memory)):

            """
            Set the actual Block size available (i.e., Size available in the block in 'i' position of the memory)
            to block_size
            """
            block_size = self.memory[i].size['available']

            """
            If the absolute value of the subtraction between block_size and process_size is less than
            last distance AND block_size is equal or greater than process_size
            (i.e. this block is more closer of the process size AND there is available space)
            THEN...
            """
            if abs(block_size - process_size) < distance and block_size >= process_size:
                """
                best_position will be settled with the current memory position
                """
                best_position = i

                """
                and I'll update the distance value, once this actual distance is less than the last one
                """
                distance = abs(block_size - process_size)

        """
        Finally, if were found some best Block available, it Address attribute will be returned
        """
        if best_position is not None:
            return self.memory[best_position].address
        else:
            """
            Else, I generate a message log informing the PID of the process that won't be allocated
            """
            support.ERRORS.append("[Warning] Could not find an available space for process {0}.".format(process.pid))

    def alloc(self, obj):
        """
        This method will receive some Process to be allocated and will pass this one for bestfit method

        :param obj: A Process Object
        :return: Block Address were the process was best allocated ;)
        """
        address = self.best_fit(obj)
        if address is not None:
            """
            Create a thread to alloc process informing the Process Object and the Block Address attribute
            where it will be allocated
            """
            my_thread = Thread(target=self.alloc_in, args=(obj, address))
            """
            Start the thread
            """
            my_thread.start()

            """
            Join the response to current context
            """
            my_thread.join()

            """
            Return the address where the Process Object was allocated
            """
            return address
        else:
            pass

    def free(self, address):
        """
        This an method tha can be helpful to clean some Process from the memory array
        :param address: A Address attribute from some block that will be cleaned
        :return: void
        """
        self.get_block(address)

    def show(self, address=None):
        """
        This method will print one particular memory block or, all memory array
        :param address: [Optional] Address attribute from some Block
        :return: list
        """
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
