# Laboratorio No.2, ruido.py
# 03/08/2021
# Integrantes:
#   - Abril Palencia, 18198
#   - Cristina Bautista, 161260

from Hamming import *
import random

class Ruido():
    def __init__(self) -> None:
        self.probabilidad = 0.365
        self.mensaje = ""
        self.antes = 0

    def meter_ruido(self, cadena):
        # Calculate the no of Redundant Bits Required
        m = len(cadena)
        r = CorreccionHamming.calcRedundantBits(m)
        
        # Determine the positions of Redundant Bits
        arr = CorreccionHamming.posRedundantBits(cadena, r)
        
        # Determine the parity bits
        arr = CorreccionHamming.calcParityBits(arr, r)

        for x in range(int(self.probabilidad)):
            pos = random.randint(0,(len(cadena)-1))
            value = str(random.randint(0,1))
            cadena = cadena[:pos] + str(value) + cadena[pos + 1:] 
        self.mensaje = cadena
        return self.mensaje, r


    def detectError(arr, nr):
        n = len(arr)
        res = 0
    
        # Calculate parity bits again
        for i in range(nr):
            val = 0
            for j in range(1, n+1):
                if(j & (2**i) == (2**i)):
                    val = val ^ int(arr[-1 * j])
                    
            # Create a binary no by appending
            # parity bits together.
    
            res = res + val*(10**i)
            
        # Convert binary to decimal
        return int(str(res), 2)