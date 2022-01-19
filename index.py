from flask import Flask, render_template, request
from NotacionPost import PostFija
from ArbolExpresiones import ArbolExpre, EvalArbolExpre

app = Flask(__name__)

@app.route('/', methods =['GET', 'POST'])
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

    '''Metodo POST'''
    if request.method == 'POST':
        valorDatos = request.form['datos']
        cadena = PostFija(valorDatos)
        resultado = str(EvalArbolExpre(cadena))

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
        limpiar = limpiar,

    )

if __name__=='__main__':
    app.run(debug=True, port=5000)

