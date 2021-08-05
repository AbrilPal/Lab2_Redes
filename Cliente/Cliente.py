# Laboratorio No.2, Cliente.py
# 29/07/2021
# Integrantes:
#   - Abril Palencia, 18198
#   - Cristina Bautista, 161260

from encode import Encode_bit 
from enviar import Enviar
from ruido import Ruido

encode_bit = Encode_bit()
enviar = Enviar()
r = Ruido()

mensaje = input("Escriba el mensaje: ")
mensaje_codificado = encode_bit.encode_cadena(mensaje)
mensaje_ruido = r.meter_ruido(mensaje_codificado)

enviar.enviar_menaje(mensaje_ruido)
