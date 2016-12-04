#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

import nano_os as myos
import json

if __name__ == "__main__":

    myos.TESTING = True

    memory_m = myos.MemoryManager()
    process_m = myos.ProcessManager()

    p1 = process_m.create("a.cpp", "allex")
    p2 = process_m.create("b.py", "daniel")
    p3 = process_m.create("c.js", "paulo")
    p4 = process_m.create("d.lua", "renan")

    print "\nProcessos:", process_m.show()
    # print "\nEspaços de Memória: ", json.dumps(memory_m.show(), indent=4)

    memory_m.alloc(process_m.get(p1))
    memory_m.alloc(process_m.get(p2))
    memory_m.alloc(process_m.get(p3))
    memory_m.alloc(process_m.get(p4))

    print "\nAlocações com o BestFit: ", json.dumps(memory_m.show(), indent=4)