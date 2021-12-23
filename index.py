from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    universidad = 'U.A.G.R.M.'
    facultad = 'F.I.C.C.T.'
    materia = 'Estructura Datos II'
    nombre = 'Jhasmany Jhunnior Fernandez Ortega'
    registro = 207025509

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
   # return "<h1>Hola mundofadfadsf-suscribite</h1>"
    return render_template(
        'home.html',
        universidad = universidad,
        facultad = facultad,
        materia=materia,
        nombre=nombre,
        registro=registro,

        uno = uno,
        dos = dos,
        tres = tres,
        cuatro = cuatro,
        cinco = cinco,
        seis = seis,
        siete = siete,
        ocho = ocho,
        nueve = nueve,
        cero=cero
    )

if __name__=='__main__':
    app.run(debug=True, port=5000)