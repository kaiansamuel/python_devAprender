#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Trabalhando com multiplas listas
from itertools import zip_longest
lista_a = ['A', 'B', 'C', 'D', 'E']
lista_b = [1,2,3,4,5,6]

for a,b in zip(lista_a, lista_b):
    print(a)
    print(b)
produtos = ['produto1', 'produto2', 'produto3', 'produto4', 'produto5']
precos = [250, 150, 220, 550, 50]
for a,b in zip(produtos, precos):
    print(f"Salvando {a} valor R$ {b}")

titulos = ['Titulo1', 'Titulo2', 'Titulo3', 'Titulo4']
descricoes = ['Descricao1', 'Descricao2', 'Descricao3']
for titulo, descricao in zip_longest(titulos, descricoes):
    print(f"Encontramos o {titulo} descrição: {descricao}")
