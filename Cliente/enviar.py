# Laboratorio No.2, enviar.py
# 03/08/2021
# Integrantes:
#   - Abril Palencia, 18198
#   - Cristina Bautista, 161260

# Libreria socket
from socket import *

class Enviar():
    def __init__(self):
        self.serverIP = "192.168.1.54"
        self.serverPort =  12000

    def enviar_menaje(self, mensaje):
        clienteSocket = socket(AF_INET, SOCK_DGRAM)
        clienteSocket.sendto(mensaje.encode(), (self.serverIP, self.serverPort))
        clienteSocket.close()