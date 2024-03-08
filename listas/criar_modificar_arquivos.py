#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Como criar e modificar arquivos:
'w' -> Usado somente para escrever algo
'a' -> Usado somente para acrescentar algo
'r' -> Usado somente para ler algo
'r+' -> Usado para ler e escrever algo
"""

import os

#with open('celulares.txt', 'w') as arquivo:
#    arquivo.write('celular2')
"""
nomes = ['lucas', 'carol', 'jeff', 'douglas']
numeros = [1,2,3,4,5,6]
with open('numeros.txt', 'a', newline='') as numeral:
    for numero in numeros:
        numeral.write(str(numero) + os.linesep)
"""
with open('nomes.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)
    arquivo.write('9000')
    
