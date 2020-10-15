from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "let'sfightinglove"

@app.route("/")
def index():
    if "cheat" not in session:
        session["cheat"] = False
    if "randnum" not in session:
        session["randnum"] = random.randint(1,100)
    print("*"*50)
    print(session)
    result = ""
    if "usernum" in session:
        if int(session["usernum"]) == int(session["randnum"]):
            session.pop("randnum")
            result = "YOU'RE A PSYCHIC WIZARD"
        elif int(session["usernum"]) > int(session["randnum"]):
            result = "TOO HIGH!"
        else:
            result = "TOO LOW!"
        session.pop("usernum")
    showme = True
    if result == "YOU'RE A PSYCHIC WIZARD":
        showme = False

    return render_template("index.html", result = result, showme = showme)

@app.route("/process", methods=["POST"])
def process():
    if "usernum" not in session:
        session["usernum"] = int(request.form["num"])
    return redirect("/")

@app.route("/cheat", methods=["POST"])
def cheat():
    session["cheat"] = True
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)