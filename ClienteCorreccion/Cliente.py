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

while True:
    mensaje = input("Escriba el mensaje: ")
    mensaje_codificado = encode_bit.encode_cadena(mensaje)
    # print("Mensaje codif", mensaje_codificado)
    mensaje_ruido, rHammning = r.meter_ruido(mensaje_codificado)
    # print("Mensaje ruido", mensaje_ruido)
    numero = Ruido.detectError(str(mensaje_ruido), rHammning)
    if (mensaje_ruido != mensaje_codificado):
        print("La posicion del error es: ", numero)
    else:
        pass

    numero_server = int(enviar.enviar_menaje(mensaje_ruido, numero))
    if(numero_server == 0):
        print("********* No hay que hacer correcciones *********")
    else:
        print("*************** Correccion en posicion ", numero_server," leyendo de derecha a izquierda ***************")

