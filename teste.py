#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

import random
import json

tamanhos = [10, 15, 20]

memoria = []
for i in range(len(tamanhos)):
    memoria.append({
        'endereco': i,
        'tamanho_t': tamanhos[i],
        'tamanho_d': tamanhos[i],
        'processos': []
    })


def processo(pid, tamanho):
    return {
        'pid': pid,
        'tamanho': tamanho
    }


def best_fit(p, m):
    distance = 1000
    best_position = None

    for x in range(0, len(m)):
        bloco_tamanho = m[x].get("tamanho_d")
        if abs(bloco_tamanho - p.get("tamanho")) < distance and p.get("tamanho") <= bloco_tamanho:
            best_position = x
            distance = abs(bloco_tamanho - p.get("tamanho"))

    if best_position is not None:
        m[best_position].get("processos").append(p)
        m[best_position].update({
            "tamanho_d": m[best_position].get("tamanho_d") - p.get("tamanho")
        })
    else:
        print "Erro ao realizar alocação do proceso {0}".format(p.get("pid"))


if __name__ == "__main__":
    for y in range(10):
        p = processo(y, 2)
        print p
        best_fit(p, memoria)

    print json.dumps(memoria, indent=4, sort_keys=True)
