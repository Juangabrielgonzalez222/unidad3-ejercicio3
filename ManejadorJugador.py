from Jugador import Jugador
class ManejadorJugador:
	__listaJugadores=[]
	def __init__(self):
		self.__listaJugadores=[]
	def agregarJugador(self,jugador):
		if type(jugador)==Jugador:
			self.__listaJugadores.append(jugador)
		else:
			print('No se pudo añadir un jugador a la lista, tipo de dato incorrecto.')
	def buscarJugador(self,dni):
		resultado=-1
		bandera=True
		i=0
		cantidadJugadores=len(self.__listaJugadores)
		while i<cantidadJugadores and bandera:
			if self.__listaJugadores[i].verificarDni(dni):
				bandera=False
				resultado=i
			else:
				i+=1
		return resultado
	def obtenerJugador(self,dni):
		resultado=-1
		iJugador=self.buscarJugador(dni)
		if iJugador!=-1:
			resultado=self.__listaJugadores[iJugador]
		return resultado
	def mostrarContratosJugador(self,dni):
		iJugador=self.buscarJugador(dni)
		if iJugador!=-1:
			self.__listaJugadores[iJugador].mostrarDatosContratos()
		else:
			print('No se encontro al jugador con el DNI ingresado')