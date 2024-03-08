#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

computador_json =""" {
    "marca": "Dell",
    "preço": 15000
 }"""
#Lendo uma string JSON
data = json.loads(computador_json)
print(data)
#Salvar uma string JSON -> Json
with open('computador.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(computador_json, arquivo_json)
with open('computador.json', encoding='utf-8') as arquivo_json:
    string_computador_json = json.load(arquivo_json)#Converte Json para string
    dicionario_computador_json = json.loads(string_computador_json)#Converte string para dicionario python
    print(dicionario_computador_json['marca'])

    
