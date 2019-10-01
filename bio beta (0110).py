from tkinter import *
import time
import hashlib
import os
from pyfingerprint.pyfingerprint import PyFingerprint

def Adicionar_Digital():
	global Tela
	Tela=Tk()
	Tela.title('bio')
	Tela.attributes('-fullscreen', True)
	Label(Tela, text = 'Iniciando...', font = 'Arial 12').pack()
	
	try:
		f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
		if ( f.verifyPassword() == False ):
			raise ValueError('The given fingerprint sensor password is wrong!')
	except Exception as e:
			exit(1)
	Label(Tela, text = 'Insira o dedo', font = "Arial 12").pack()
	try:
		print('botodeda1')
		while(f.readImage() == False):
			pass
		f.convertImage(0x01)
		result=f.searchTemplate()
		positionNumber= result[0]
		if (positionNumber >= 0):
			print('já tem')
			exit(0)
		Label(Tela, text = 'Remova', font = 'Arial 12').pack()
		time.sleep(2)
		Label(Tela, text = 'Insira o mesmo dedo', font = "Arial 12").pack()
		while ( f.readImage() == False ):
			pass
		f.convertImage(0x02)
		if ( f.compareCharacteristics() == 0 ):
			raise Exception('Fingers do not match')
		f.createTemplate()
		print('Finger enrolled successfully!')
		Label(Tela, text = 'Registrado!!!!!!!!', font = 'Arial 12').pack()
	except Exception as e:
		print('Operation failed!')
		print('Exception message: ' + str(e))
		exit(0)
	Tela.mainloop()
	
Adicionar_Digital
