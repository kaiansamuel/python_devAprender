#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import itemgetter
nomes = ['Zack', 'Camilla', 'Julius', 'Homer'] 
valores = [31,23,4,36, 23,33,37,7,20,23]
pessoas = [
    {
     'nome': 'John',
     'idade': 32,
     'nivel_acesso': 2
    },
    {
     'nome': 'Carol',
     'idade': 18,
     'nivel_acesso': 3        
    },
    {
     'nome': 'Thomas',
     'idade': 45,
        'nivel_acesso': 5   
    },
    {
     'nome': 'Ana',
     'idade': 23,
     'nivel_acesso': 5   
    }    
]
pessoas.sort(key=itemgetter('nome'))
print(pessoas)
