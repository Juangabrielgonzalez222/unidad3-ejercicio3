from Contrato import Contrato
class Equipo:
    __idEquipo=0
    __nombre=''
    __ciudad=''
    __listaContratos=[]
    def __init__(self,idEquipo=0,nombre='',ciudad=''):
        self.__idEquipo=idEquipo
        self.__nombre=nombre
        self.__ciudad=ciudad
        self.__listaContratos=[]
    def agregarContrato(self,contrato):
        if type(contrato)==Contrato:
            self.__listaContratos.append(contrato)
        else:
            print('Error, no se pudo agregar un contrato a la lista, el tipo de datos es incorrecto.')
    def verificarId(self,id):
        resultado=False
        if self.__idEquipo==id:
            resultado=True
        return resultado
    def verificarNombre(self,nombre):
        resultado=False
        if self.__nombre==nombre:
            resultado=True
        return resultado
    def buscarJugadorEnContrato(self,dni):
        resultado=-1
        bandera=True
        i=0
        cantidadContratos=len(self.__listaContratos)
        while i<cantidadContratos and bandera:
            if self.__listaContratos[i].verificarJugadorPorDNI(dni):
                resultado=i
                bandera=False
            else:
                i+=1
        return resultado
    def mostrarNombre(self):
        print('Nombre:',self.__nombre)
    def getNombre(self):
        return self.__nombre
    def calcularImporteTotal(self):
        importe=0
        for contrato in self.__listaContratos:
            importe+=contrato.calcularImporte()
        print('El importe total en contratos del equipo {} es de:{}'.format(self.__nombre,importe))
    def mostrarContratosPorVencimiento(self):
        for contrato in self.__listaContratos:
            contrato.mostrarDatosPorVencimiento()
    def __str__(self):
        return 'ID:{} Nombre:{} Ciudad:{}'.format(self.__idEquipo,self.__nombre,self.__ciudad)