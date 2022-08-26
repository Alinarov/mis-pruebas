from pygame import *

import pygame

pygame.init()

class main:
	def __init__(self,nombre,edad):
		self.nombre = nombre
		self.edad = edad

		self.__main__() # llamamos la funcion
		pass
		
	def __main__(self):
		if self.nombre == "ermenegildo":
			print("ola ermenegildo")
		else:
			pass

		if self.edad == 12:
			print("tiene eda de 12")
		else:
			pass
		pass

	def __call__():

		pass



# construimos el objeto
persona = main("ermenegildo",12)



