#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"O nome é {self.name} e tem {self.age} anos."

person1 = Person('Kaian', 42) 
person2 = Person('Mauriceia', 38)

print(person1)
print(person2)
