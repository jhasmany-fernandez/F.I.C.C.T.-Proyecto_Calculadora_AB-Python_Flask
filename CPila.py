# CLASE PILA

from CNodo import Nodo

class Pila:
    def __init__(self):
        self.__tope = None

    '''Comprueba si la pila esta vacia.'''
    def vacia(self):
        return self.__tope is None

    '''Devuelve el elemento de la cima de la pila.'''
    def cima(self):
        if (not self.vacia()) :
            return self.__tope.dato
        else:
            return None

    '''Mete un nuevo elemento a la pila'''
    def meter(self , val):
        aux = Nodo()
        aux.dato = val
        aux.der = self.__tope
        self.__tope = aux

    '''Extrae el elemento de la cima de la pila.'''
    def sacar(self):
        e = None       
        if (not self.vacia()):
            aux = Nodo()
            e = self.__tope.dato
            aux = self.__tope
            self.__tope = self.__tope.der
            del aux
        return e 
    '''Imprime los elementos contenidos en la pila.'''
    def imprimir(self):
        aux = Pila() 
        e = None
        while not self.vacia():
            e = self.sacar()
            aux.meter(e) 
            print(e)   
        while not aux.vacia():
            e = aux.sacar()
            self.meter(e)

if __name__ == "__main__":
    pila = Pila()
    pila.meter(1)
    pila.meter(2)
    pila.meter(3)

    pila.imprimir()
   
    
 
