"""
CLASE NODO
"""
class Nodo:
    def __init__(self, valor=None):
        self.__der = None
        self.__izq = None
        self.__dato = valor

    @property
    def dato(self):  
        """
        Getter del atibuto dato.
        """     
        return self.__dato 

    @dato.setter 
    def dato(self, valor): 
        """
        Setter del atributo dato.
        """     
        self.__dato = valor

    @property
    def izq(self):
        """
        Getter del atributo hijo izquierdo.
        """
        return self.__izq

    @izq.setter 
    def izq(self, nodo):
        """
        Setter del atributo hijo izquierdo.
        """
        self.__izq = nodo

    @property
    def der(self):
        """
        Getter del atributo hijo derecho.
        """
        return self.__der

    @der.setter 

    def der(self, nodo):
        """
        Setter del atributo hijo derecho.
        """
        self.__der = nodo