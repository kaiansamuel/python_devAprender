#!/usr/bin/env python
# -*- coding: utf-8 -*-

from array import array

numeros = array('i', [1,2,3,4,5,6,7])
print(numeros)
numeros.append(10)
print(numeros)
numeros.insert(5, 200)
print(numeros)
numeros.pop(1)
print(numeros)
numeros.remove(5)
print(numeros)
del numeros[1]
print(numeros)

