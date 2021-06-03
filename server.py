from socket import *
from ecb import dec
from ecb import stringToBinary

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
key = bin(67).replace("0b", "")

while True:
  serverSocket.listen(1)
  print("[SERVER] The server is wait for connection..")
  connection, clientAddress = serverSocket.accept()
  print('[SERVER] Got connection from ', clientAddress)
  
  connected = True
  
  while connected:
    encrypted_message_length = connection.recv(2048).decode()
    encrypted_message_length = int(encrypted_message_length)
    encrypted_message = connection.recv(encrypted_message_length).decode()
    
    print('[Client] encrypted message: '+ str(encrypted_message))
    encrypted_binary = stringToBinary(encrypted_message) 
    print('[Server] convert to binary('+ str(len(encrypted_binary))+ '): ' +encrypted_binary+ "\n")
    message = dec(encrypted_message, key)
    if (message == 'DC'):
      print('[Server] received Disconnect Message')
      connected = False
      
    ##sendback
    connection.send(('Decrypted Message: '+ message + '\n').encode())
    
  if(connected == False):
    print('[SERVER] Connection from '+str(clientAddress[0])+ ':'+ str(clientAddress[1])+ ' is disconnected\n')
    
  connection.close()
