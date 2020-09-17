from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import domain

app = Flask(__name__)
CORS(app)

@app.route('/', methods=["GET"])
def pocetna():
    return "Server je pokrenut!"

@app.route('/prijava', methods=['POST', "GET"])
def prijava():
    podaci = request.get_json()
    email = podaci.get('email')
    lozinka = podaci.get('lozinka')
    print('S => ', email, lozinka)
    korisnik = domain.prijava(email, lozinka)
    return jsonify({
            'status': 'uspjesno',
            'korisnik': korisnik
        })

@app.route('/registracija', methods=['POST'])
def registracija():
    podaci = request.get_json()
    ime = podaci.get('ime')
    email = podaci.get('email')
    lozinka = podaci.get('lozinka')
    tel = podaci.get('tel')
    grad = podaci.get('grad')
    status = domain.registracija(ime, email, lozinka, tel, grad)
    if (status):
        return jsonify({
                'status': 'uspjesno'
            })
    else:
        return jsonify({
                'status': 'neuspjesno'
            })

@app.route('/izmjena', methods=['POST'])
def izmjena():
    podaci = request.get_json()
    id = podaci.get('id')
    email = podaci.get('email')
    tel = podaci.get('tel')
    status = domain.izmjene_podataka(id, email, tel)
    if (status):
            return jsonify({
                    'status': 'uspjesno'
                })
    else:
        return jsonify({
                'status': 'neuspjesno'
            })

@app.route('/institucije', methods=['GET'])
def institucije():
    institucije = domain.dohvatiInstitucije()
    return jsonify({
        'status': 'uspjesno',
        'institucije': institucije
    })

if __name__ == '__main__':
    app.run(debug=True)
