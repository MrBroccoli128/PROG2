#####
# Die Applikation wurde unter folgenden Umständen entwickelt und getestet.
# PyCharm 2019.3.1 (Professional Edition)
# Build #PY-193.5662.61, built on December 18, 2019
# Runtime version: 11.0.5+10-b520.17 x86_64
# VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# macOS 10.15.1
# Non-Bundled Plugins: AceJump, izhangzhihao.rainbow.brackets, net.vektah.codeglance, org.sonarlint.idea
# Browser: Firefox 72.0.1 x64
#####


### SACHEN WELCHE NÄCHSTES MAL ANDERS GEMACHT WERDEN:
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


# Loginpage für die Kursuebersicht
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        att_user = str(request.form['username'])
        att_pass = str(request.form['password'])
        # Überprüfung des Logins
        if verify_login(att_user, att_pass) is True:
            # Falls korrekt, wird eine Session mit Cookie erstellt
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
    # Bei einem POST kann es sich nur um eine Anmeldung handeln.
    if request.method == 'POST':
        # Eine Überprüfung der Werte ist nicht nötig, da alle Felder im HTML auf required stehen.
        course = str(request.form['btn'])
        sign_vorname = str(request.form['vorname'])
        sign_nachname = str(request.form['nachname'])
        sign_geb = str(request.form['geb'])
        sign_address = str(request.form['address'])
        sign_ort = str(request.form['ort'])

        # Aufruf der Funktion um den neuen Teilnehmer am Kurs anzumelden
        add_student(sign_vorname, sign_nachname, sign_geb, sign_address, sign_ort, course)

        flash("Sich haben sich erfolgreich für den Kurs " + course + " angemeldet!")
    # Ausgeben der Hauptseite mit den aktuellen verfügbaren Kursen
    return render_template('main.html', c_list=c_list.items())


# Route für die Kursleiteransicht
@app.route('/kursleiter/', methods=['GET', 'POST'])
def kursleiter():
    if request.method == 'POST':
        # Ein POST aus dem Button mit dem value create bedeutet die Erstellung eines neuen Kurses
        if "create" in request.form["btn"]:
            i_titel = str(request.form['title'])
            i_beschreibung = str(request.form['beschreibung'])
            i_datum = str(request.form['datum'])
            i_zeit = str(request.form['zeit'])
            i_minT = int(request.form['minT'])
            i_maxT = int(request.form['maxT'])
            i_ort = str(request.form['ort'])
            # Die maximale Anzahl Teilnehmer muss grösser sein als die Minimal Anzahl
            if i_minT > i_maxT:
                flash("Mindestanzahl ist grösser als die Maximalanzahl von Teilnehmer")
            else:
                # Kurs wird mithilfe der Funktion hinzugefügt
                add_kurs(i_titel, i_beschreibung, i_datum, i_zeit, i_minT, i_maxT, i_ort, session['username'])
        # Ein POST mit dem Button delete bedeutet, das löschen eines kurses
        elif "delete" in request.form["btn"]:
            coursename = request.form["btn"].split(";")
            # Übergabe des Kursnamens an die Löschfunktion
            del_kurs(coursename[1])
    # Darstellen der aktuellen Kursübersicht
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


# 400 Error abfangen
@app.errorhandler(400)
def error_400(e):
    return render_template('400.html')


if __name__ == '__main__':
    # Cookie encryption durch einen random int
    app.secret_key = urandom(20)
    app.run(debug=True, port=5000)
