# Laboratorio No.2, Server.py
# 29/07/2021
# Integrantes:
#   - Abril Palencia, 18198
#   - Cristina Bautista, 161260

# Libreria socket
from socket import *

# Puerto del servidor
serverPort = 12000
# Socket del servidor
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Bind address
serverSocket.bind(('', serverPort))
# mensaje del servidor
print("el server ya esta escuchando en el puerto: " , serverPort)

while True:
    mensaje, clientAddress = serverSocket.recvfrom(2048)
    mensajeCodificado = mensaje.decode().upper()
    serverSocket.sendto(mensajeCodificado.encode(), clientAddress)
