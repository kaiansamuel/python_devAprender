#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
#Criar e ler JSON existente
usuarios_json = """{
    "name": "John Smith",
    "age": 30,
    "city": "New York",
    "isStudent": true,
    "gpa": 3.5
}"""

#Salvar uma string Json -> arquivo Json
with open('desafio.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(usuarios_json, arquivo_json)

    
