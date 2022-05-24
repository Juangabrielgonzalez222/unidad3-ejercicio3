from Contrato import Contrato
class Jugador:
    __nombre=''
    __dni=''
    __ciudadNatal=''
    __paisDeOrigen=''
    __fechaNacimiento=None
    __listaContratos=[]
    def __init__(self,nombre='',dni='',ciudadNatal='',paisDeOrigen='',fechaNacimiento=None):
        self.__nombre=nombre
        self.__dni=dni
        self.__ciudadNatal=ciudadNatal
        self.__paisDeOrigen=paisDeOrigen
        self.__fechaNacimiento=fechaNacimiento
        self.__listaContratos=[]
    def agregarContrato(self,contrato):
        if type(contrato)==Contrato:
            self.__listaContratos.append(contrato)
        else:
            print('Error, no se pudo agregar un contrato a la lista, el tipo de datos es incorrecto.')
    def getDNI(self):
        return self.__dni
    def verificarDni(self,dni):
        resultado=False
        if self.__dni==dni:
            resultado=True
        return resultado
    def mostrarDatosContratos(self):
        for contrato in self.__listaContratos:
            contrato.mostrarDatosEquipoYFecha()
    def __str__(self):
        return 'Nombre:{}, DNI:{},Ciudad:{},Pais de origen:{}, Fecha de nacimiento:{}'.format(self.__nombre,self.__dni,self.__ciudadNatal,self.__paisDeOrigen,self.__fechaNacimiento.strftime("%d/%m/%Y"))