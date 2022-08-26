class persona(object):
	"""docstring for ClassName"""
	def __init__(self, edad, nombre):
		self.edad = edad
		self.nombre = nombre
	def hablar(self,nombre):
		print("ola ",nombre)
		print("tienes la edad de ",self.edad)
		
class ing_sistemas(persona):
	def programar(self, lenguaje):
		print("wa programar",lenguaje)

class lic_derecho(persona):
	def estudiar_caso(self,de):
		print("debo estudiar_caso",de)

ermenegildo = persona(23,"ermenegildo")

ermenegildo.hablar("ermenegildo")
