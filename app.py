#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

import m_manager as myos

if __name__ == "__main__":
    process_m = myos.ProcessManager()
    p1 = process_m.create("teste_p.cpp", "allexlima")
    p2 = process_m.create("teste_p.cpp", "allexlima")
    print process_m.show()
    print "apagando processo p1..."
    process_m.delete(p1)
    print process_m.show()
