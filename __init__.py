from flask import Flask, render_template, request, flash


app = Flask("__main__")

@app.route("/main/")
def main():
    return render_template('main.html')

@app.route("/", methods=['GET', 'POST'])
def page():
    return "hey"


if __name__ == "__main__":
    app.run(debug=True, port=5000)