#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Herança
class Camera:
    def __init__(self, marca, megapixels):
        self.marca = marca
        self.megapixels = megapixels

    def tirar_foto(self):
        print(
        f'Foto tirada com uma camera {self.marca} com a qualidade de {self.megapixels} megapixels'
        )

class CameraCelular(Camera):
    def __init__(self, marca, megapixels, quantidades_de_cameras):
        super().__init__(marca, megapixels)
        self.quantidade_de_cameras = quantidades_de_cameras

    def aplicar_filtro(self, filtro):
        print(f'Aplicando filtro {filtro}')

    def tirar_foto(self, camera_a_utilizar):
        print(
        f'Foto tirada com a camera {self.marca} com a qualidade de {self.megapixels} megapixels')

camera_celular = CameraCelular('Sony', '25mp', 4)
camera_celular.aplicar_filtro('Azul')
camera_celular.tirar_foto(2)
        
