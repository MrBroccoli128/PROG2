from flask import Flask, render_template, request, flash, url_for, redirect
from user_functions import verify_login
from kurs_mgmt import *

app = Flask('__main__')


# Weiterleitung auf das Loginfenster wenn auf das Rootverzeichnis zugegriffen wird
@app.route('/')
def root():
    return redirect(url_for('main'))


@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        att_user = str(request.form['username'])
        att_pass = str(request.form['password'])

        if verify_login(att_user, att_pass) is True:
            flash(att_pass)
            flash(att_user)
            return redirect(url_for('main'))
        else:
            return render_template('login.html')
    return render_template('login.html')


@app.route("/main/", methods=['GET', 'POST'])
def main():
    c_list = get_course_list()
    if request.method == 'GET':
        return render_template('main.html', c_list=c_list.items())
    elif request.method == 'POST':
        return redirect(url_for('signup', signed_course=str(request.form['signup'])))


@app.route("/main/signup", methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':
        course = request.args['signed_course']
        sign_vorname = str(request.form['vorname'])
        sign_nachname = str(request.form['nachname'])
        sign_geb = str(request.form['geb'])
        sign_address = str(request.form['address'])
        sign_ort = str(request.form['ort'])
        # Ob alle Felder ausgefüllt wurde wird in der HTML Form überprüft

        add_student(sign_vorname, sign_nachname, sign_geb, sign_address, sign_ort, course)

        return "Erfolgreich angemeldet"
    else:
        return render_template('anmeldung_kurs.html', c_info=get_course_list()[request.args['signed_course']],
                               signed_course=request.args['signed_course'])


# 404 Error abfangen
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True, port=5000)
