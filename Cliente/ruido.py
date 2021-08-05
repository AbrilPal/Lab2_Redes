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
        self.probabilidad = 0.2
        self.mensaje = ""

    def meter_ruido(self, cadena):
        self.probabilidad = int(len(cadena) * self.probabilidad)
        dec = ft.fletcher32(cadena, len(cadena))
        print(dec)
        for x in range(self.probabilidad):
            pos = random.randint(0,99)
            value = str(random.randint(0,1))
            cadena = cadena[:pos] + str(value) + cadena[pos + 1:]

            print('Ruido en:','pos', pos,'value', value)    

        self.mensaje = cadena + dec
