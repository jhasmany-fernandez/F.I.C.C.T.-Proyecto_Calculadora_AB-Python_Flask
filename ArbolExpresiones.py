
import sys
from CNodo import Nodo
from CPila import Pila
from NotacionPost import PostFija
 
'''Metodo que crea un arbol de expresiones y 
     devuelve la raiz de dicho arbol. '''
def ArbolExpre(cadena):
  operador = "+-*/"
  pila = Pila()
  for char in cadena:
    nod = Nodo()
    nod.dato = char
    if char in operador:
      nod.der = pila.sacar()
      nod.izq = pila.sacar()
    pila.meter(nod)  
  return pila.cima()   

def EsDecimal(val):
   val = str(val)
   indice = val.find(".")
   if indice == -1:
     return False
   return True  

'''Metodo que evalua un arbol de expresiones y 
     devuelve el resultado de dicha evaluacion.'''
def EvalArbolExpre(root):
  if root is not None:
    if (root.izq == None and root.der == None):
      d = float(root.dato) if EsDecimal(root.dato) else int(root.dato)
      return d
    a = EvalArbolExpre(root.izq)
    b = EvalArbolExpre(root.der)
    if (root.dato == '+'):
      return a+b 
    elif(root.dato == '-'):
      return a-b
    elif(root.dato == '*'):
      return a*b
    else:
      try:
        return a/b         
      except ZeroDivisionError:        
        """
        print("NO SE PUEDE DIVIDIR ENTRE CERO") 
        return sys.exit() #Termina el programa
        """
        return "DC"

if __name__ == "__main__" :  
  expr = input("Inserte la Expresion: ")
  cadena = PostFija(expr)  
  root = ArbolExpre(cadena)  
  print("El resultado es: "+ str(EvalArbolExpre(root)))

      
  
 
  


  
  
  

  
