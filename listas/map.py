#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Como criar listas
#Criando com o range

numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)

#Processando com o Map

nomes = ['Larissa', 'Rafael', 'Marcus', 'Jhon']

def aprovar_pessoa(nome):
    return nome + ' APROVADO'

print(list(map(aprovar_pessoa, nomes)))

