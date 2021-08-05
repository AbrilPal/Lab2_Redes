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

    def enviar_menaje(self, mensaje, numero):
        clienteSocket = socket(AF_INET, SOCK_DGRAM)
        clienteSocket.sendto(str(mensaje).encode(), (self.serverIP, self.serverPort))
        print("-----------------------enviado exitosamente-----------------------")
        # lo que recibe del server
        numero_server, serverAddress = clienteSocket.recvfrom(2048)
        numero = int(numero_server.decode())
        print("respuesta del server: ", numero)
        clienteSocket.close()
        return numero_server.decode()