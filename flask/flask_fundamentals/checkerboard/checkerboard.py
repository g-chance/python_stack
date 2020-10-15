from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", num=8, num2=8)

@app.route("/<number>")
def indexNumber(number):
    return render_template("index.html", num=int(number), num2= 8)

@app.route("/<number>/<number2>")
def indexNumber2(number, number2):
    return render_template("index.html", num=int(number), num2=int(number2))

if __name__ == "__main__":
    app.run(debug=True)