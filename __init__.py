from flask import Flask, render_template, request, flash, url_for, redirect
from user_functions import verify_login
from kurs_mgmt import *

app = Flask("__main__")

# Weiterleitung auf das Loginfenster wenn auf das Rootverzeichnis zugegriffen wird
@app.route("/")
def root():
    return redirect(url_for("login"))


@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        att_user = str(request.form['username'])
        att_pass = str(request.form['password'])


        if verify_login(att_user, att_pass) is True:
            flash(att_pass)
            flash(att_user)
            return render_template('main.html')
        else:
            return render_template('login.html')
    return render_template('login.html')


@app.route("/main/",  methods=['GET', 'POST'])
def main():
    return 0

# 404 Error abfangen
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True, port=5000)