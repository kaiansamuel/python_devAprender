#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

computador_json = {
    "marca": "Dell",
    "preço": 15000
 }

data = json.loads(computador_json)
print(data["preço"])
