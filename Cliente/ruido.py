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
        self.antes = 0

    def meter_ruido(self, cadena):
        self.probabilidad = int(len(cadena) * self.probabilidad)
        largo = len(cadena)
        self.antes = ft.fletcher32(cadena, largo)
        for x in range(self.probabilidad):
            pos = random.randint(0,(len(cadena)-1))
            value = str(random.randint(0,1))
            cadena = cadena[:pos] + str(value) + cadena[pos + 1:] 
        self.mensaje = cadena
        return self.mensaje

    def detectar(self):
        return self.antes