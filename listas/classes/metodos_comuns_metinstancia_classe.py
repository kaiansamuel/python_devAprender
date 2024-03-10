#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Computador:
    sistema_operacional = 'Windows 10'

    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def exibir_dados_computador(self):
        print(self.marca, self.memoria_ram,
              self.placa_de_video, self.sistema_operacional)

    @classmethod
    def computador_escritorio(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Video - Baixo Custo')

    @classmethod
    def computador_configuracao_pesada(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Video - Alto Nivel')

    @staticmethod
    def roda_programas_pesados(memoria_ram):
        if memoria_ram >= 8:
            return True
        else:
            return False

# Configuração p/ cliente de escritorio
computador1 = Computador.computador_escritorio('8gb')
# Configuração p/ cliente de trabalho pesado(jogos, videos, 3d)
computador2 = Computador.computador_configuracao_pesada('16gb')
computador1.exibir_dados_computador()
print(Computador.roda_programas_pesados(10))
print('='*15)

