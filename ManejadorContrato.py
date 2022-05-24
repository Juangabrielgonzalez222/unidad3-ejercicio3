import csv,numpy as np
from Contrato import Contrato
class ManejadorContrato:
    __arregloContratos=None
    __cantidad=0
    __dimension=0
    __incremento=0
    def __init__(self,dimension=3,incremento=5):
        self.__arregloContratos=np.empty(dimension,dtype=Contrato)
        self.__dimension=dimension
        self.__incremento=incremento
        self.__cantidad=0
    def agregarContrato(self,contrato):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arregloContratos.resize(self.__dimension)
        self.__arregloContratos[self.__cantidad]=contrato
        self.__cantidad+=1
    def generarArchivo(self):
        nombreArchivo='Contratos.csv'
        archivo=open(nombreArchivo,'w',encoding='utf-8',newline='')
        writer=csv.writer(archivo,delimiter=';')
        writer.writerow(['DNI','Nombre del equipo','Fecha de inicio','Fecha de fin','Pago mensual'])
        for i in range(self.__cantidad):
            self.__arregloContratos[i].guardarDatosAlArchivo(writer)
        archivo.close()