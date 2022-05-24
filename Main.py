from ManejadorContrato import ManejadorContrato
from ManejadorEquipo import ManejadorEquipo
from ManejadorJugador import ManejadorJugador
from Menu import Menu

if __name__== '__main__':
	manejadorEquipo=ManejadorEquipo(3,5)
	manejadorContrato=ManejadorContrato(3,5)
	manejadorJugador=ManejadorJugador()
	manejadorEquipo.cargarDesdeArchivo()
	menu=Menu()
	menu.lanzarMenu(manejadorEquipo,manejadorContrato,manejadorJugador)