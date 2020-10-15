from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_form():
    name = request.form["name"]
    email = request.form["email"]
    radio = request.form["poop"]
    checkbox = request.form.getlist("colors")
    print("**"*50)
    # print (radio)
    return  render_template("stuff.html", name=name, email=email, radio=radio, checkbox=checkbox)

if __name__ == "__main__":
    app.run(debug=True)