from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play/<num>/<myColor>")
def index(num, myColor):
    return render_template("index.html", num=int(num), bgColor=myColor)

if __name__ == "__main__":
    app.run(debug=True)