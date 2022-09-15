import socket
from commands import commands_info, commands
from encrypt_decrypt import encrypt

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 6900
host = socket.gethostname()
server.bind((host, port))

server.listen()
print('Server listening on port ', port)

while True:
  conn, addr = server.accept()
  print('Connection has been established with client. Client Address: ', addr)

  conn.send(commands_info().encode())

  mode = conn.recv(1024).decode()
  encrypted_command = conn.recv(1024).decode()

  response, status = commands(mode, encrypted_command)
  encrypted_response = encrypt(mode, response)
  encrypted_status = encrypt(mode, status)

  conn.send(encrypted_response.encode())
  conn.send(encrypted_status.encode())