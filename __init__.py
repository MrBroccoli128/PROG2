#####
# Die Applikation wurde unter folgenden Umständen entwickelt und getestet.
# OS: macOS 10.15 Catalina
# Browser: Firefox 69.0.2 x64
#####
####
# NEXT STEP:
# Session variable ist definiert. Login gegencheck funktioniert.
# Seite der Kursleiter erstellen. Usermanagement!

### SACHEN WELCHE ANDERS GEMACHT WERDEN SOLLTEN:
# kursname nicht key des dict
# Teilnehmer der Kurs nicht vollständig im kurs dict
###


from flask import Flask, render_template, request, flash, url_for, redirect, session
from os import urandom  # Random Funktion
from user_functions import verify_login  # Enthält die Funktionen, welche mit dem Userhandling in Verbindung stehen
from kurs_mgmt import add_student, get_course_list, \
    add_kurs, del_kurs  # Funktionen, welche mit der Kursadministration zu tun haben

app = Flask('__main__')


# Weiterleitung auf die Hauptseite wenn auf das Rootverzeichnis zugegriffen wird
@app.route('/')
def root():
    return redirect(url_for('main'))


# Loginpage
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        att_user = str(request.form['username'])
        att_pass = str(request.form['password'])

        if verify_login(att_user, att_pass) is True:

            session['logged_in'] = True
            session['username'] = str(request.form['username'])
            return redirect(url_for('kursleiter'))
        else:
            # Ausgabe der Fehlermeldung
            flash("Der Benutzername oder das Passwort waren falsch")
            # Damit der Login erneut versucht werden kann, kommt man wieder auf die gleiche Seite wie beim GET
            return render_template('login.html')
    return render_template('login.html')


# Hauptseite
@app.route('/main/', methods=['GET', 'POST'])
def main():
    # Für die Darstellung der Kursübersicht müssen die Kurse aus der JSON Datei geladen werden.
    c_list = get_course_list()
    if request.method == 'GET':
        return render_template('main.html', c_list=c_list.items())
    # Bei einem POST kann es sich nur um eine versuchte Anmeldung handeln.
    elif request.method == 'POST':
        return redirect(url_for('course_signup', signed_course=str(request.form['signup'])))


# Anmeldung an einem Kurs
@app.route("/main/signup/", methods=['GET', 'POST'])
def course_signup():
    if request.method == 'POST':
        course = request.args['signed_course']  # Variable aus der URL abgreifen
        sign_vorname = str(request.form['vorname'])
        sign_nachname = str(request.form['nachname'])
        sign_geb = str(request.form['geb'])
        sign_address = str(request.form['address'])
        sign_ort = str(request.form['ort'])
        # Ob alle Felder ausgefüllt wurde wird in der HTML Form überprüft

        add_student(sign_vorname, sign_nachname, sign_geb, sign_address, sign_ort, course)

        return render_template('anmelde_bestaetigung.html', signed_course=course, sign_vorname=sign_vorname,
                               sign_nachname=sign_nachname)
    else:
        return render_template('anmeldung_kurs.html', c_info=get_course_list()[request.args['signed_course']],
                               signed_course=request.args['signed_course'])


@app.route('/kursleiter/', methods=['GET', 'POST'])
def kursleiter():
    if request.method == 'POST':
        if "create" in request.form["btn"]:
            i_titel = str(request.form['title'])
            i_beschreibung = str(request.form['beschreibung'])
            i_datum = str(request.form['datum'])
            i_zeit = str(request.form['zeit'])
            i_minT = int(request.form['minT'])
            i_maxT = int(request.form['maxT'])
            i_ort = str(request.form['ort'])

            if i_minT > i_maxT:
                flash("Mindestanzahl ist grösser als die Maximalanzahl von Teilnehmer")
            else:
                add_kurs(i_titel, i_beschreibung, i_datum, i_zeit, i_minT, i_maxT, i_ort, session['username'])
        elif "delete" in request.form["btn"]:
            coursename = request.form["btn"].split(";")
            print(coursename[1])
            del_kurs(coursename[1])



    c_list = get_course_list()
    return render_template('kursleiter.html', c_list=c_list.items())


# Wenn der User logout klickt soll die Session verworfen werden
@app.route("/logout/")
def logout():
    flash("Sie haben sich sich ausgeloggt!")
    session.clear()
    return redirect(url_for('main'))


# 404 Error abfangen
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(400)
def error_400(e):
    return render_template('400.html')


if __name__ == '__main__':
    # Cookie encryption durch einen random int
    app.secret_key = urandom(20)
    app.run(debug=True, port=5000)
