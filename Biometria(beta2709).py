from tkinter import *
import time
import hashlib
import os
from pyfingerprint.pyfingerprint import PyFingerprint
from login2 import *

#def Usr_ja_cad():
	
	
#def Dedos_nao_batem():
	
	
#def Usr_nao_enc():
	
	


def Buscar_Digital():
	global sc_bioSrc
	sc_bioSrc = Toplevel(screen2)
	sc_bioSrc.title("Biometria")
	sc_bioSrc.attributes('fullscreen',True)
	try:
		f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
		if( f.verifyPassword() == False ):
			raise ValueError('The given fingerprint sensor password is wrong!')
	except Exception as e:
		user_not_found()
		exit(1)
	try:
		while ( f.readImage() == False ):
			pass
		f.convertImage(0x01)

		result = f.searchTemplate()

		positionNumber = result[0]
		accuracyScore = result[1]
		if ( positionNumber == -1 ):
			user_not_found()
			exit(0)
		else:
			Finger=positionNumber
			Lista= os.listdir()
		if Finger in Lista:
			Ver=open(Finger+".fin", 'r')
			usr=Ver.read().splitlines()
	except Exception as e:
		exit(1)

def Adicionar_Digital():
	global sc_bioAdd
	sc_bioAdd = Toplevel(screen2)
	sc_bioAdd.title("Biometria")
	sc_bioAdd.attributes('fullscreen',True)
	Label(sc_bioAdd, text = "bota o dedin aí", font = "Arial 12").pack()
	try:
		f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
		if ( f.verifyPassword() == False ):
			raise ValueError('The given fingerprint sensor password is wrong!')
	except Exception as e:
			exit(1)
	try:
		Label(sc_bioAdd, text = "bota o dedin aí", font = "Arial 12").pack()
		while(f.readImage() == False):
			pass
		f.convertImage(0x01)
		result=f.searchTemplate()
		positionNumber= result[0]
		if (positionNumber >= 0):
			user_not_found()
			exit(0)
			Label(sc_bioAdd, text = "tira o dedin aí", font = "Arial 12").pack()
			time.sleep(2)
			Label(sc_bioAdd, text = "bota o dedin aí denovo", font = "Arial 12").pack()
			while(f.readImage() == False):
				pass
		f.convertImage(0x02)
		if (f.compareCharacteristics() == 0 ):
			raise Exception("Fingers not Match")
			password_not_recognised()
		f.createTemplate()
		positionNumber = f.storeTemplate()
		USR=open(positionNumber+".fin")
		USR.write(usr)
		USR.close
		Cadastrado()
		main_screen()
	except Exception as e:
		exit(1)

def Remover_Digital():
	global sc_bioRem
	sc_bioRem = Toplevel(screen2)
	sc_bioRem.title("Biometria")
	sc_bioRem.attributes('fullscreen',True)
	try:
		f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
	
		if ( f.verifyPassword() == False ):
			raise ValueError('The given fingerprint sensor password is wrong!')
			
			
	except Exception as e:
		exit(1)
	try:
		positionNumber = input('Please enter the template position you want to delete: ')
		positionNumber = int(positionNumber)
		if ( f.deleteTemplate(positionNumber) == True ):
			print('Template deleted!')
	except Exception as e:
		print('Operation failed!')
		print('Exception message: ' + str(e))
		exit(1)

		
