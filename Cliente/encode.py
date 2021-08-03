# Laboratorio No.2, encode.py
# 29/07/2021
# Integrantes:
#   - Abril Palencia, 18198
#   - Cristina Bautista, 161260

#librerias
from bitarray import bitarray

class Encode_bit():
    def __init__(self):
        self.mensaje_codificado = ""

    def encode_cadena(self, mensaje):
        bit = bitarray()
        bit.frombytes(mensaje.encode())
        self.mensaje_codificado = str(bit.to01())
        # print(self.mensaje_codificado)
        return self.mensaje_codificado