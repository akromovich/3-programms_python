import pyAesCrypt


password = input('Введите пароль: ')

encrypte = pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)
