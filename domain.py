import sqlite3
import uuid

def create_connection():
    try:
        db = sqlite3.connect('baza.db')
        return db
    except:
        return None

def prijava(email, lozinka):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Korisnik WHERE email = ? AND lozinka = ?", (email, lozinka))
    korisnik = cursor.fetchone()
    print('KORISNIK: ', korisnik)
    conn.close()
    return korisnik

def registracija(ime, email, lozinka, tel, grad):
    conn = create_connection()
    cursor = conn.cursor()
    id = uuid.uuid4().hex
    cursor.execute("INSERT INTO Korisnik VALUES (?, ?, ?, ?, ?, ?)", (id, ime, email, lozinka, tel, grad))
    conn.commit()
    conn.close()
    return id

def izmjene_podataka(id, email, tel):
    conn = create_connection()
    cursor = conn.cursor()
    print('POD: ', id, email, tel)
    cursor.execute("UPDATE Korisnik SET email = ?, tel = ? WHERE id = ?", (email, tel, id))
    conn.commit()
    conn.close()
    return id

def dohvatiInstitucije():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Institucija")
    institucije = cursor.fetchall()
    conn.close()
    return institucije
