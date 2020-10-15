from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo"

@app.route("/say/<name>")
def name(name):
    return "Hello, " + name +"!"

@app.route("/repeat/<num>/<text>")
def repeat(num, text):
    return (text+"<br>")*int(num)

# This only works if the user doesn't enter another "/" after the text
@app.route("/<text>")
def error(text):
    if text != "dojo" and text != "say" and text != "repeat":
        return "YOU SUCK"

if __name__ == "__main__":
    app.run(debug=True)