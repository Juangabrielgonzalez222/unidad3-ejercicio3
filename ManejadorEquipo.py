import csv,numpy as np
from Equipo import Equipo
class ManejadorEquipo:
    __arregloEquipos=None
    __cantidad=0
    __dimension=0
    __incremento=0
    def __init__(self,dimension=3,incremento=5):
        self.__arregloEquipos=np.empty(dimension,dtype=Equipo)
        self.__dimension=dimension
        self.__incremento=incremento
        self.__cantidad=0
    def agregarEquipo(self,equipo):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.redimensionarArreglo()
        self.__arregloEquipos[self.__cantidad]=equipo
        self.__cantidad+=1
    def redimensionarArreglo(self):
        self.__arregloEquipos.resize(self.__dimension)
    def cargarDesdeArchivo(self):
        nombreArchivo='Equipos.csv'
        archivo=open(nombreArchivo,encoding='utf-8')
        reader=csv.reader(archivo,delimiter=';')
        banderaCantidad=True
        for fila in reader:
            if banderaCantidad:
                try:
                    self.__dimension=int(fila[0])
                except:
                    print('Ocurrio un error al leer la cantidad de equipos en la primera linea del archivo.')
                else:
                    self.redimensionarArreglo()
                banderaCantidad=False
            else:
                self.agregarEquipo(Equipo(self.__cantidad+1,fila[0],fila[1]))
        print('Fin de la carga desde: ',nombreArchivo)
    def mostrarEquipos(self):
        print('Equipos:')
        for i in range(self.__cantidad):
            print(self.__arregloEquipos[i])
    def buscarEquipoId(self,id):
        resultado=-1
        bandera=True
        i=0
        while i <self.__cantidad and bandera:
            if self.__arregloEquipos[i].verificarId(id):
                bandera=False
                resultado=i
            else:
                i+=1
        return resultado
    def buscarEquipoNombre(self,nombre):
        resultado=-1
        bandera=True
        i=0
        while i <self.__cantidad and bandera:
            if self.__arregloEquipos[i].verificarNombre(nombre):
                bandera=False
                resultado=i
            else:
                i+=1
        return resultado
    def obtenerEquipo(self,id,dniJugador):
        resultado=-1
        iEquipo=self.buscarEquipoId(id)
        if iEquipo!=-1:
            contratoConJugador=self.__arregloEquipos[iEquipo].buscarJugadorEnContrato(dniJugador)
            if contratoConJugador==-1: #Contrato no existe
                resultado=self.__arregloEquipos[iEquipo]
            else:
                resultado=-2
        return resultado
    def mostrarContratosDelEquipo(self,id):
        iEquipo=self.buscarEquipoId(id)
        if iEquipo!=-1:
            self.__arregloEquipos[iEquipo].mostrarContratosPorVencimiento()
        else:
            print('El numero de identificador ingresado no corresponde a ningun equipo.')
    def calcularImporteTotalDelEquipo(self,nombreEquipo):
        iEquipo=self.buscarEquipoNombre(nombreEquipo)
        if iEquipo!=-1:
            self.__arregloEquipos[iEquipo].calcularImporteTotal()
        else:
            print('No se encontro un equipo con el nombre ingresado.')