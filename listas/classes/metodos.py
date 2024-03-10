#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Métodos de uma classe -> ligar, desligar, exibir dados do computador
class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def ligar(self):
        print('Estou ligando o computador')
    
    def desligar(self):
        print('Estou desligando o computador')
    
    def exibir_dados_do_computador(self):
        print(
            f"Computador da marca {self.marca}, com {self.memoria_ram} de memoria ram e que usa a placa de video {self.placa_de_video}"
            )
computador1 = Computador('Asus', '32gb', 'NVidia')
computador1.ligar()
computador1.desligar()
computador1.exibir_dados_do_computador()
