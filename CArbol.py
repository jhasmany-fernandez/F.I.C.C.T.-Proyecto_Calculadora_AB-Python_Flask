"""
CLASE ARBOL
"""
from CNodo import Nodo

class Arbol:     
    def __init__(self):
        self.__root = None
        

    @property
    def root(self):
        """
        Getter del atributo root.
        """
        return self.__root

    @root.setter 
    def root(self, nodo):
        """
        Setter del atributo root.
        """
        self.__root = nodo         


    def Vacio(self):
        """
        Comprueba si la raiz esta vacia.
        """
        return  self.__root is None   
    
    
    def Insertar(self, dat):
        """
        Inserta un dato al arbol.
        """
        
        if self.Vacio() :
            self.root = Nodo(dat)
        else:            
            self.__Insert(dat, self.root)
            

    def __Insert(self, dat , nodo):
        """
        Metodo llamado por Insetar(), que recorre recursivamente 
        el arbol hasta insertar el nuevo dato.
        """
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
                 



    def InOrden(self, raiz):
        """
        Recorrido InOrden.
        """
        if raiz is not None :
            self.InOrden(raiz.izq)
            print(raiz.dato, end=" ")
            self.InOrden(raiz.der)

    def PreOrden(self, raiz):
        """
        Recorrido PreOrden.
        """
        if raiz is not None:
            print(raiz.dato, end=" ") 
            self.PreOrden(raiz.izq)
            self.PreOrden(raiz.der) 

    def PostOrden(self, raiz):
        """
        Recorrido PostOrden.
        """
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









    