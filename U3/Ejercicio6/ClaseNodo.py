from ClaseAparatos import aparato

class nodo:
    __aparato = None
    __siguiente = None

    def __init__(self,aparato:aparato):
        self.__aparato = aparato
        self.__siguiente = None
    
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__aparato