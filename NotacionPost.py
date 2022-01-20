# MODULO CON SOLO METODOS.
# POSTFIJA() ES EL METODO USADO PARA TRANSFORMAR UNA NOTACION INFIJA A POSTFIJA
# SIENDO LOS DEMAS METODOS UTILZIADOS POR ESTE.

import sys
from CPila import Pila
p = Pila()

'''Devuelve True si en caracter es un numero.'''
def EsNum(dato):
    num = ["0","1","2","3","4","5","6","7","8","9","."]    
    for n in dato:
        if n  not in num:
            return False                     
    return True  

'''Devuelve True si el caracter es un parentesis
    de apertura.'''
def EsPareIzq(dato):
    b = True if dato == "(" else False
    return b

'''Devuelve True si el caracter es un parentesis 
    de cierre.'''
def EsPareDere(dato):
    b = True if dato == ")" else False
    return b

'''Devuelve True si el caracter es un operador.'''
def EsOperador(dato):
    b = True if dato in "+-*/" else False
    return b  
    
'''Devuelve el nivel de precedencia del operador'''
def Precedencia(dato):
    if dato in "+-":
        return 1
    elif dato in "*/":
        return 2
    else:
        return 0

def EsPunto(dato):
    b = True if dato == "." else False
    return b

'''Introduce la expresion en una lista.'''
def ListaE(expre):
    num = ""
    lista = []
    for char in expre:
        if EsNum(char) or EsPunto(char):
            num += char
            if len(expre) == 1:
                lista.append(num)  
                return lista       
        else:
            if  num:
                if num[0] == "." or num[len(num)-1] == ".":
                    return "ES"
                lista.append(num)
                num = ""           
            lista.append(char)            
    if  num:
        if num[0] == "." or num[len(num)-1] == ".":
            return "ES"
        lista.append(num)        
    return lista

'''Analiza una expresion, para determinar si existe un error de sintaxis "ES"'''
def Analizar(lista):
    c = 0
    op = "/*-+"    
    if len(lista) > 2:
        while c < len(lista):
            if c == 0:
                if not(EsNum(lista[0]) or lista[0] == "("):
                    return "ES"
            elif c == (len(lista)-1) :
                if not(EsNum(lista[c]) or lista[c] == ")"):
                    return "ES"
            else:
                if (lista[c] in op):
                    if (lista[c-1] in ".(/*-+" or lista[c+1] in ")./*-+"):
                        return "ES"
                elif EsNum(lista[c]):
                    if (lista[c-1] == ")" or lista[c+1] == "("):
                        return "ES"
                elif lista[c] == "(":
                    if (lista[c-1] in ")." or EsNum(lista[c-1]) or lista[c+1] in ")./*-+"):
                        return "ES"
                elif lista[c] == ")":
                    if (lista[c-1] in "./*-+" or lista[c+1] == "(." or EsNum(lista[c+1])):
                        return "ES"
                else:
                    if lista[c] == ".":
                        if not(EsNum(lista[c-1]) and EsNum(lista[c+1])):
                            return "ES"
            c += 1 
    elif len(lista) == 2:
        if (lista[0] in ")./*-+"):
            return "ES"
        if (EsNum(lista[0])):
            if not(lista[1] in "/*-+."):
                return "ES"
        else:
            if (lista[1] in "/*-+)."):
                return "ES"
        return "ND"        
    else:
        if (lista[0] in "/*-+.)"):
            return "ES" 
        return "ND"           

'''Convierte una expresion a notacion postfija y
    devuelve una lista'''
def PostFija(cadena):
    expre = ListaE(cadena)  
    if expre == "ES":
        return "ES"   
    if (expre.count("(") != expre.count(")")):
        """
        print("NUMERO DE PARENTESIS ERRONEO")
        return sys.exit() #Termina el programa si hay un error en el numero de parentesis.
        """
        return "EP"
    Error = Analizar(expre) 
    if Error == "ES":
        return "ES"
    elif Error == "ND":
        return "ND"    
    final =[]  
    s = prece  = None   
    for dato in expre:        
        if EsNum(dato):
            final.append(dato)
        elif EsPareIzq(dato):
            p.meter(dato)
        elif EsPareDere(dato):
            while (p.cima() != "(" and not p.vacia()):
               s = p.sacar()
               final.append(s)
            if (p.cima() == "("):
                s = p.sacar()                         
        elif EsOperador(dato):
            while (not p.vacia() and ( Precedencia(dato) <= Precedencia(p.cima()) ) ):
                s = p.sacar()
                final.append(s)
            p.meter(dato)
        else:
            print("ENTRADA INVALIDA")
            return sys.exit() #Termina el programa si se inserta una entrada incorrecta   
    while (not p.vacia()):
        s = p.sacar()
        final.append(s) 
    if len(final) == 1:
        return "ND"
    print("La notacion postfija es: ")
    print(final)
    return final

if __name__ == "__main__":
    cad = input("Intoduce la expresion: ")
    PostFija(cad)
    

   







 


