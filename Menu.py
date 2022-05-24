from datetime import date
from Contrato import Contrato
from Jugador import Jugador
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.opcion4,
            5:self.opcion5,
            6:self.salir
        }
    def lanzarMenu(self,manejadorEquipo,manejadorContrato,manejadorJugador):
        #Menu opciones
        i=len(self.__opciones)
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1 para crear un contrato para un jugador en un equipo.')
            print('-Ingrese 2 para consultar un jugador contratado ingresando un DNI.')
            print('-Ingrese 3 para ingresar el identificador de un Equipo y listar los datos de los Jugadores cuyo contrato vence en 6 meses.')
            print('-Ingrese 4 para para dado un nombre de equipo, determinar el importe total de los contratos que posee con los jugadores del equipo.')
            print('-Ingrese 5 para guardar contratos.')
            print('-Ingrese 6 para salir.')
            opcion=self.cargarNumeroEntero('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion==1:
                ejecutar(manejadorEquipo,manejadorContrato,manejadorJugador)
            elif opcion==2:
                ejecutar(manejadorJugador)
            elif opcion>2 and opcion<5:
                ejecutar(manejadorEquipo)
            elif opcion==5:
                ejecutar(manejadorContrato)
            else:
                ejecutar()
    def opcion1(self,manejadorEquipo,manejadorContrato,manejadorJugador):
        print('Ingrese DNI del jugador, si el DNI ya corresponde a algun jugador, no se requeriran los datos del mismo.')
        dni=input('Ingrese DNI:\n')
        jugadorExiste=True
        jugador=manejadorJugador.obtenerJugador(dni)
        if jugador==-1:
            print('No se encontro al jugador, a continuacion debe cargar los datos del mismo:')
            jugadorExiste=False
            nombre=input('Nombre:\n')
            ciudad=input('Ciudad natal:\n')
            pais=input('Pais de origen: ')
            print('A continuacion debe ingresar la fecha de nacimiento:')
            fechaNacimiento=self.cargarFecha()
            jugador=Jugador(nombre,dni,ciudad,pais,fechaNacimiento)
        print('A continuacion debe seleccionar el equipo, o si quiere salir ingrese s:')
        bandera=True
        equipo=None
        salir=False
        while bandera:
            manejadorEquipo.mostrarEquipos()
            idEquipo=input('Ingrese un numero de equipo o s para salir:')
            if idEquipo=='s':
                bandera=False
                salir=True
            else:
                try:
                    idEquipo=int(idEquipo)
                except ValueError:
                    print('Solo se admiten numeros enteros o s para cancelar la carga')
                else:
                    equipo=manejadorEquipo.obtenerEquipo(idEquipo,dni)
                    if equipo==-1:
                        print('No se encontro el equipo con el numero ingresado.')
                    elif equipo==-2:
                        print('El equipo seleccionado, ya posee un contrato con el jugador.')
                    else:
                        bandera=False
        if not salir:
            print('A continuacion se solicitaran datos del contrato:')
            print('Fecha de inicio del contrato:')
            fechaInicio=self.cargarFecha()
            print('Fecha de finalizacion del contrato:')
            fechaFin=self.cargarFecha()
            pagoMensual=0.0
            bandera=True
            while bandera:
                try:
                    pagoMensual=float(input('Pago Mensual:\n'))
                except ValueError:
                    print('Solo se aceptan numeros enteros y punto, por ejemplo:1000 o 1000.55')
                else:
                    bandera=not bandera
            contrato=Contrato(fechaInicio,fechaFin,pagoMensual,equipo,jugador)
            jugador.agregarContrato(contrato)
            equipo.agregarContrato(contrato)
            manejadorContrato.agregarContrato(contrato)
            if not jugadorExiste:
                manejadorJugador.agregarJugador(jugador)
        else:
            print('Se cerro de la carga.')
    def opcion2(self,manejadorJugador):
        dni=input('Ingrese DNI:\n')
        manejadorJugador.mostrarContratosJugador(dni)
    def opcion3(self,manejadorEquipo):
        manejadorEquipo.mostrarEquipos()
        id=self.cargarNumeroEntero('Ingrese el numero de equipo:\n')
        manejadorEquipo.mostrarContratosDelEquipo(id)
    def opcion4(self,manejadorEquipo):
        nombreEquipo=input('Ingrese nombre del equipo:\n')
        manejadorEquipo.calcularImporteTotalDelEquipo(nombreEquipo)
    def opcion5(self,manejadorContrato):
        manejadorContrato.generarArchivo()
    def cargarNumeroEntero(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('ERROR: Se debe ingresar un numero entero.')
            else:
                bandera=False
        return numero
    def cargarFecha(self):
        fecha=None
        bandera=True
        while bandera:
            try:
                dia=int(input('Dia:\n'))
                mes=int(input('Mes:\n'))
                año=int(input('Año:\n'))
                fecha=date(año,mes,dia)
            except ValueError as e:
                print('Uno de los valores ingresados no es correcto, vuelva a intentarlo.')
            else:
                bandera=False
        return fecha
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')