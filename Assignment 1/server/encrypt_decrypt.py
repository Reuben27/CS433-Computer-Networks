def transpose(data):
  encrypt_data = ""

  #Split data into sentences and then into words. Finally reverse each word.
  for sentence in data.split('\n'):
    for word in sentence.split(' '):
      reversed_word = word[::-1]
      encrypt_data += reversed_word
      encrypt_data += ' '
    encrypt_data += '\n'
  
  return encrypt_data.strip()

def decrypt_transpose(encrypt_data):
  data = ""

  #Split data into sentences and then into words. Finally reverse each word to get back original word.
  for sentence in encrypt_data.split('\n'):
    for word in sentence.split(' '):
      reversed_word = word[::-1]
      data += reversed_word
      data += ' '
    data += '\n'
  
  return data.strip()

def substitute(data, offset):
  encrypt_data = ""
  for character in data:
    if (character.isupper()):
      encrypt_data += chr((ord(character) + offset-65) % 26 + 65)

    elif (character.islower()):
      encrypt_data += chr((ord(character) + offset-97) % 26 + 97)

    elif(character.isnumeric()):
      encrypt_data += str(int(character) + offset) if (int(character) + offset) <= 9 else str((int(character) + offset - 10))

    else:
      encrypt_data += character

  return encrypt_data.strip()

def decrypt_substitute(encrypt_data, offset):
  data = ""
  for character in encrypt_data:
    if (character.isupper()):
      data += chr((ord(character) + offset-65) % 26 + 65)

    elif (character.islower()):
      data += chr((ord(character) + offset-97) % 26 + 97)

    elif(character.isnumeric()):
      data += str(int(character) + offset) if (int(character) + offset) >= 0 else str((int(character) + offset + 10))

    else:
      data += character

  return data.strip()

def encrypt(mode, data):
  if (int(mode) == 1):
    return data
  elif (int(mode) == 2):
    return substitute(data, 2)
  elif (int(mode) == 3):
    return transpose(data)

def decrypt(mode, encrypt_data):
  if (int(mode) == 1):
    return encrypt_data
  elif (int(mode) == 2):
    return decrypt_substitute(encrypt_data, -2)
  elif (int(mode) == 3):
    return decrypt_transpose(encrypt_data)