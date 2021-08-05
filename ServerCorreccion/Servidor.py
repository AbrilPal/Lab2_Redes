# Laboratorio No.2, Server.py
# 29/07/2021
# Integrantes:
#   - Abril Palencia, 18198
#   - Cristina Bautista, 161260

# Libreria socket
from socket import *
from ruido import CorreccionHammingServer

r = CorreccionHammingServer()

# Puerto del servidor
serverPort = 4308
# Socket del servidor
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Bind address
serverSocket.bind(('', serverPort))
# mensaje del servidor
print("el server ya esta escuchando en el puerto: " , serverPort)

while True:
    mensaje, clientAddress = serverSocket.recvfrom(2048)
    mensajeCodificado = mensaje.decode()

    m = len(mensajeCodificado)
    rHamming = CorreccionHammingServer.calcRedundantBits(m)
    arr = CorreccionHammingServer.posRedundantBits(mensajeCodificado, rHamming)
    arr = CorreccionHammingServer.calcParityBits(arr, rHamming)

    print("Mensaje recibido: ", mensajeCodificado)
    numero_f = str(CorreccionHammingServer.detectError(arr, rHamming))
    # numero_f = '1'
    print("Mensaje enviado:",numero_f)
    serverSocket.sendto(numero_f.encode(), clientAddress)
