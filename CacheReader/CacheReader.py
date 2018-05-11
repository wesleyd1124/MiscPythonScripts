from os import listdir
from os.path import isfile, join
import binascii
import ctypes, sys


path = input("Enter Path : ")

readFiles = [f for f in listdir(path)]

for file in readFiles:
	content = ""
	with open(path+"\\"+file, 'rb') as f:
		content = f.read()
	content = binascii.hexlify(content)
	headers = [b"8950", b"1f8b"]
	headerFileTypes = ["png", "gzip"]
	
	for header in headers:
		i = 0
		if(content[:len(header)] == header):
			print(file + " is a " + headerFileTypes[i])
			break
		else:
			print(content[:len(header)])
		i = i + 1