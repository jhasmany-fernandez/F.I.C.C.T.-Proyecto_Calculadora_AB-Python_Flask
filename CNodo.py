# CLASE NODO

class Nodo:
    def __init__(self, valor=None):
        self.__der = None
        self.__izq = None
        self.__dato = valor

    '''Getter del atibuto dato.'''
    @property
    def dato(self):
        return self.__dato 

    '''Setter del atributo dato.'''
    @dato.setter 
    def dato(self, valor):
        self.__dato = valor

    '''Getter del atributo hijo izquierdo.'''
    @property
    def izq(self):
        return self.__izq

    '''Setter del atributo hijo izquierdo.'''
    @izq.setter 
    def izq(self, nodo):
        self.__izq = nodo

    '''Getter del atributo hijo derecho.'''
    @property
    def der(self):
        return self.__der

    '''Setter del atributo hijo derecho.'''
    @der.setter
    def der(self, nodo):
        self.__der = nodo