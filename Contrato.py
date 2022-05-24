class Contrato:
    __fechaDeInicio=None
    __fechaDeFin=None
    __pagoMensual=0
    __equipo=None
    __jugador=None
    def __init__(self,fechaInicio=None,fechaFin=None,pagoMensual=0,equipo=None,jugador=None):
        from Equipo import Equipo
        from Jugador import Jugador
        if type(equipo)!=Equipo:
            print('Error, el contrato esperaba un equipo, pero el tipo de datos no coincide.')
            self.__equipo=None
        else:
            self.__equipo=equipo
        if type(jugador)!=Jugador:
            print('Error, el contrato esperaba un jugador, pero el tipo de datos no coincide.')
            self.__jugador=None
        else:
            self.__jugador=jugador
        self.__fechaDeInicio=fechaInicio
        self.__fechaDeFin=fechaFin
        self.__pagoMensual=pagoMensual
    def verificarJugadorPorDNI(self,dni):
        resultado=False
        if self.__jugador.verificarDni(dni):
            resultado=True
        return resultado
    def mostrarDatosEquipoYFecha(self):
        self.__equipo.mostrarNombre()
        print('Fecha de finalizacion del contrato:',self.__fechaDeFin.strftime("%d/%m/%Y"))
    def calcularMeses(self):
        meses=0
        cantidadDias=self.__fechaDeFin-self.__fechaDeInicio
        meses=round(cantidadDias.days/30.417,2)
        return meses
    def calcularVencimientoSeisMeses(self):
        resultado=False
        resultadoResta=self.__fechaDeFin-self.__fechaDeInicio
        if resultadoResta.days<365/2:
            resultado=True
        return resultado
    def mostrarDatosPorVencimiento(self):
        meses=self.calcularMeses()
        if meses<=6:
            print(self.__jugador)
    def calcularImporte(self):
        importe=0
        meses=self.calcularMeses()
        importe=meses*self.__pagoMensual
        return importe
    def guardarDatosAlArchivo(self,writer):
        writer.writerow([self.__jugador.getDNI(),self.__equipo.getNombre(),self.__fechaDeInicio.strftime("%d/%m/%Y"),self.__fechaDeFin.strftime("%d/%m/%Y"),str(self.__pagoMensual)])