#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Enumerate
for indice, numero in enumerate(range(1, 11), 1):
    print(indice, numero)
    if indice == 5:
        print('Estamos na metade da lista')
nomes = ['nome1', 'nome2', 'nome3', 'nome4']
for indice, nome in enumerate(nomes, 1):
    print(indice, nome)
    if indice == 3:
        print('Já temos 3 pessoas registradas')

