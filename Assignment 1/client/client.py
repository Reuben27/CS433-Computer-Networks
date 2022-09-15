import socket
from encrypt_decrypt import encrypt, decrypt

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 6900
host = socket.gethostname()
client.connect((host, port))

server_message = client.recv(1024).decode()
print("Received the following from server: \n", server_message)

mode = 1
print('''The following encryption modes are available:
  1 - Plain Text
  2 - Substitute
  3 - Transpose
''')

command = input('Enter command: ').strip()

while True:
  mode = input('Enter mode of encryption: ').strip()
  if(int(mode) >= 1 and int(mode) <=3):
    break
  else:
    print("Mode of encryption not available. Try again!")

if(command.split(' ')[0] == "UPD" or command.split(' ')[0] == "upd"):
  try:
    path = command[4:]
    f = open(path, 'r')
    data = f.read(2048)
    f.close()
    command = "UPD " + data
  except:
    command = "UPD"

encrypted_command = encrypt(mode, command)

client.send(mode.encode())
client.send(encrypted_command.encode())

encrypted_response = client.recv(1024).decode()
encrypted_status = client.recv(1024).decode()

response = decrypt(mode, encrypted_response)
status = decrypt(mode, encrypted_status)

if(command.split(' ')[0] == "DWD" or command.split(' ')[0] == "dwd"):
  if(status == "OK"):
    try:
      f = open('downloaded_file.txt', 'w')
      f.write(response)
      f.close()
    except:
      response = "Error in writing to file!"
      status = "NOK"

print("Status from the server: \n", status)
print("Response from the server: \n", response)

client.close()
print('Connection Closed')