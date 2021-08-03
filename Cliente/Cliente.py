# Laboratorio No.2, Cliente.py
# 29/07/2021
# Integrantes:
#   - Abril Palencia, 18198
#   - Cristina Bautista, 161260

# Libreria socket
from socket import *
from encode import Encode_bit 

encode_bit = Encode_bit()

serverIP = "192.168.1.54"
serverPort =  12000
clienteSocket = socket(AF_INET, SOCK_DGRAM)
mensaje = input()
clienteSocket.sendto(encode_bit.encode_cadena(mensaje), (serverIP, serverPort))
mensajeCodificado, serverAddress = clienteSocket.recvfrom(2048)
print(mensajeCodificado.decode())
clienteSocket.close()
