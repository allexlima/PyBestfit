#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

import m_manager as myos
import json

if __name__ == "__main__":
    process_m = myos.ProcessManager()
    p1 = process_m.create("teste_p1.cpp", "juca")
    p2 = process_m.create("teste_p2.py", "allex")
    p3 = process_m.create("teste_p3.js", "fulano")
    # print "PID dos processos criados: {0}, {1} e {2}. \nApagando processo {1}...\n".format(p1, p2, p3)
    process_m.kill(p2)
    # print json.dumps(process_m.show(p2), indent=4, sort_keys=True)
    memory = myos.Memory()
    print json.dumps(memory.show(), indent=4, sort_keys=True)
