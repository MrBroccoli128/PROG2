from flask import Flask
from flask import render_template

app = Flask("Hello World")

@app.route('/hello')
def hello_world():
    name = "Jonathan2"
    return render_template('index.html', name=name, ha="Vogel")

@app.route("/test")
def test():
    return "success"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
