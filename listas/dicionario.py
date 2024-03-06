#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Dicionarios
pessoa = {'nome': 'Carol', 'idade': 18, 'altura': 1.60}
pessoa2 = dict(nome= 'Carol', idade= 18, altura= 1.60)
print(pessoa)
print(pessoa2)
#Acessar as chaves
print(pessoa2.keys())
#Acessar todos os itens
print(pessoa.values())
print(pessoa.items())
#iterar sobre um dicionario
for item in pessoa.items():
    print(item[1])

