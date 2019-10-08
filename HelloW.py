from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask("__main__")
Bootstrap(app)
@app.route('/hello')
def hello_world():
    name = "Jonathan2"
    return render_template('index.html', name=name, ha="Vogel")


@app.route("/test")
def test():
    return "success"


@app.route("/", methods=['GET', 'POST'])
def tr():
    if request.method == 'POST':
        z1 = int(request.form['zahl1'])
        z2 = int(request.form['zahl2'])
        z3 = int(request.form['zahl3'])
        summe = str(z1 + z2 + z3)
        return render_template("ergebnis.html", sum=summe)
    return render_template("taschenrechner.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)