# Laboratorio No.2, Cliente.py
# 29/07/2021
# Integrantes:
#   - Abril Palencia, 18198
#   - Cristina Bautista, 161260

from encode import Encode_bit 
from enviar import Enviar

encode_bit = Encode_bit()
enviar = Enviar()

mensaje = input("Escriba el mensaje: ")
mensaje_codificado = encode_bit.encode_cadena(mensaje)
enviar.enviar_menaje(mensaje_codificado)
