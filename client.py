from socket import *
from ecb import enc

serverName = 'localHost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

def send(msg):
    message = msg.encode()
    message_length = len(message)
    send_length= str(message_length).encode()
    clientSocket.send(send_length)
    clientSocket.send(message)
    
n = int(input('banyaknya anggota kelompok: '))
key = bin(67).replace("0b", "") #key

for i in range(n):
    message = input('input Nama(spasi)NIM: ')
    encrypted_message = enc(message, key)
    send(encrypted_message)

    # menerima pesan dari server
    modifiedMessage = clientSocket.recv(2048)
    print('[SERVER] ' + modifiedMessage.decode())
    
send(enc('DC', key)) ## disconnect a connection
clientSocket.close()
