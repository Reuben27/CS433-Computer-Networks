import os
from encrypt_decrypt import decrypt

def commands_info():
  return ''' The following commands are supported:
    1. CWD - Retrieve the path of the current working directory for the user
    2. LS - List the files/folders present in the current working directory
    3. CD <dir> - Change the directory to <dir> as specified by the client
    4. DWD <file> - Download the <file> specified by the user on server to client
    5. UPD <file> - Upload the <file> on client to the remote server in CWD
  '''

def commands(mode, encrypted_command):
  command = decrypt(mode, encrypted_command)
  response = ""
  status = ""
  
  if (command == 'cwd' or command == 'CWD'):
    response = os.getcwd()
    status = "OK"

  elif (command == 'ls' or command == 'LS'):
    response = "Directory List: \n"
    for i in os.listdir():
      response += i + "\n"
    status = "NOK"

  elif (command.split(' ')[0] == "cd" or command.split(' ')[0] == "CD"):
    try:
      path = command[3:]
      os.chdir(path)
      curr_dir = os.getcwd()
      response = 'Directory has been changed to ' +  curr_dir
      status = "OK"
    except:
      response = 'Directory does not exist!'
      status = "NOK"

  elif (command.split(' ')[0] == "dwd" or command.split(' ')[0] == "DWD"):
    try:
      path = command[4:].strip()
      f = open(os.path.join(os.curdir, path), 'r')
      response = f.read(2048)
      f.close()
      status = "OK"
    except:
      response = 'File does not exist!'
      status = "NOK"

  elif (command.split(' ')[0] == "upd" or command.split(' ')[0] == "UPD"):
    try:
      if(len(command) < 4):
        raise Exception()
      data = command[4:]
      f = open('uploaded_file.txt', 'w')
      f.write(data)
      f.close()
      response = "File has been uploaded to server."
      status = "OK"
    except:
      response = 'File could not be uploaded!'
      status = "NOK"

  else:
    response = "Command not available."
    status = "NOK"

  return response, status