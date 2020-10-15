from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "let'sfightinglove"

@app.route("/")
def index():
    if "totalgold" not in session:
        session["totalgold"] = 0
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    if "message" not in session:
        session["message"] = ""
    if request.form["findgold"] == "farm":
        find = random.randint(10,20)
        session["totalgold"] += find
        session["message"] += "<p class='earn'>Earned "+str(find)+" gold at the Farm!</p>"
    elif request.form["findgold"] == "cave":
        find = random.randint(5,10)
        session["totalgold"] += find
        session["message"] += "<p class='earn'>Earned "+str(find)+" gold at the Cave!</p>"
    elif request.form["findgold"] == "house":
        find = random.randint(2,5)
        session["totalgold"] += find
        session["message"] += "<p class='earn'>Earned "+str(find)+" gold at the House!</p>"
    elif request.form["findgold"] == "casino":
        find = random.randint(-50,50)
        session["totalgold"] += find
        if find < 0:
            session["message"] += "<p class='lost'>Lost "+str(find*-1)+" gold at the Casino!</p>"
        else:
            session["message"] += "<p class='earn'>Earned "+str(find)+" gold at the Casino!</p>"
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)