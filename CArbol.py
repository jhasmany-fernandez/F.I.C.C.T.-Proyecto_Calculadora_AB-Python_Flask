# CLASE ARBOL
from CNodo import Nodo

class Arbol:     
    def __init__(self):
        self.__root = None
        
    '''Getter del atributo root.'''
    @property
    def root(self):
        return self.__root

    '''Setter del atributo root.'''
    @root.setter 
    def root(self, nodo):
        self.__root = nodo         

    '''Comprueba si la raiz esta vacia.'''
    def Vacio(self):
        return  self.__root is None   
    
    '''Inserta un dato al arbol.'''
    def Insertar(self, dat):
        if self.Vacio() :
            self.root = Nodo(dat) # crea un nodo y lo inserta en la raiz
        else:            
            self.__Insert(dat, self.root) # llama a esta funcion auxiliar y le pasa la raiz
            
    '''Metodo llamado por Insetar(), que recorre recursivamente 
        el arbol hasta insertar el nuevo dato.'''
    def __Insert(self, dat , nodo):
        if nodo is None:
            nodo = Nodo(dat)
        else:
            if dat < nodo.dato:
                if nodo.izq is None:
                    nodo.izq = Nodo(dat)
                else:
                    self.__Insert(dat, nodo.izq)
            elif dat > nodo.dato:
                if nodo.der is None:
                    nodo.der = Nodo(dat)
                else:
                    self.__Insert(dat, nodo.der)   
                 
    '''Recorrido InOrden.'''
    def InOrden(self, raiz):
        if raiz is not None :
            self.InOrden(raiz.izq)
            print(raiz.dato, end=" ")
            self.InOrden(raiz.der)

    '''Recorrido PreOrden.'''
    def PreOrden(self, raiz):
        if raiz is not None:
            print(raiz.dato, end=" ") 
            self.PreOrden(raiz.izq)
            self.PreOrden(raiz.der) 

    '''Recorrido PostOrden'''
    def PostOrden(self, raiz):
        if raiz is not None:
            self.PostOrden(raiz.izq)
            self.PostOrden(raiz.der)
            print(raiz.dato)

if __name__ == "__main__":

    Raiz = Arbol() 
    Raiz.Insertar(21)          
    Raiz.Insertar(13)
    Raiz.Insertar(15)    
    Raiz.Insertar(10)
    Raiz.Insertar(18)
    Raiz.Insertar(25)
    Raiz.Insertar(40)

    Raiz.InOrden(Raiz.root)









    