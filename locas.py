import os
os.system('pip install colorama')
os.system('pip install pyAesCrypt')
os.system('pip install colorama')
import pyAesCrypt
import pyfiglet
from colorama import init, Fore
print(Fore.GREEN+'\t my Friend Farzam') 
print(Fore.GREEN+pyfiglet.figlet_format('LOCAS'))
print(Fore.WHITE+'\tEncoder and Decoder File')
txt = input (Fore.RED+'Enter Encode(y) / Decode(n) : ')
txt = txt.upper()
if txt == 'Y':
	print("<Encrypt>")
	bufferSize = 64 * 1024

	file = input("File Name : ")
	password = input("Password : ")

	pyAesCrypt.encryptFile(file,file+".aes",password,bufferSize)
if txt == 'N':
	print("File Encrypted !")
	print("<Decrypt>")
	bufferSize = 64 * 1024
	file = input("File Name : ")
	password = input("Password : ")
try:
    pyAesCrypt.decryptFile(file,file+"_decrypted",password,bufferSize)
    print("File Decrypted !")
except:
    print('error')
    exit(1)
