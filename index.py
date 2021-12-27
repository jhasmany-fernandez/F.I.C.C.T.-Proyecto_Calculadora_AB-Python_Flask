from flask import Flask, render_template, request
from NotacionPost import PostFija
from ArbolExpresiones import ArbolExpre, EvalArbolExpre

app = Flask(__name__)

@app.route('/')
def index():

    '''Datos Personales'''
    universidad = 'U.A.G.R.M.'
    facultad = 'F.I.C.C.T.'
    materia = 'Estructura Datos II'
    nombre = 'Jhasmany Jhunnior Fernandez Ortega'
    registro = 207025509

    '''Numeros'''
    uno = 1
    dos = 2
    tres = 3
    cuatro = 4
    cinco = 5
    seis = 6
    siete = 7
    ocho = 8
    nueve = 9
    cero = 0

    '''Operadores'''
    suma = '+'
    resta = '-'
    multiplicacion = '×'
    division = '÷'

    '''Complementos'''
    igual = '='
    punto = '.'
    limpiar = 'AC'

    return render_template(
        'home.html',
        universidad = universidad, # '''Datos Personales'''
        facultad = facultad,
        materia=materia,
        nombre=nombre,
        registro=registro,

        uno = uno, # '''Numeros'''
        dos = dos,
        tres = tres,
        cuatro = cuatro,
        cinco = cinco,
        seis = seis,
        siete = siete,
        ocho = ocho,
        nueve = nueve,
        cero=cero,

        suma = suma, # '''Operadores'''
        resta = resta,
        multiplicacion = multiplicacion,
        division = division,

        igual = igual, # '''Complementos'''
        punto = punto,
        limpiar = limpiar
    )
'''

@app.route('/calculator', methods=['POST'])
def metoPost():
    valorIngresado = request.form['']
    cadena = PostFija(valorIngresado)
    root = ArbolExpre(cadena)
    return root
'''

@app.route('/usuario', methods=['POST'])
def usuario():
    nombreUser = request.form['nombreUser']
    return "<h1>Bienvenido " + nombreUser + "</h1>"

if __name__=='__main__':
    app.run(debug=True, port=5000)
    expr = input("Inserte la Expresion: ")
    cadena = PostFija(expr)
    root = ArbolExpre(cadena)
    print("El resultado es: " + str(EvalArbolExpre(root)))