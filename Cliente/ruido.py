# Laboratorio No.2, ruido.py
# 03/08/2021
# Integrantes:
#   - Abril Palencia, 18198
#   - Cristina Bautista, 161260

from Fletcher import Deteccion
import random

ft = Deteccion()

class Ruido():
    def __init__(self) -> None:
        self.probabilidad = 0.365
        self.mensaje = ""

    def meter_ruido(self, cadena):
        print(cadena)
        self.probabilidad = int(len(cadena) * self.probabilidad)
        largo = len(cadena)
        print(largo)
        dec = ft.fletcher32(cadena, largo)
        print(dec)
        for x in range(self.probabilidad):
            pos = random.randint(0,(len(cadena)-1))
            value = str(random.randint(0,1))
            cadena = cadena[:pos] + str(value) + cadena[pos + 1:]  
        print(len(cadena))
        self.mensaje = cadena
        return self.mensaje
