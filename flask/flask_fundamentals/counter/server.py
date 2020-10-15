from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "let'sfightinglove"

@app.route("/plustwo", methods=["POST"])
def indexpost():
    print(session)
    session["count"] += 1
    print(session)
    session["actualcount"] -= 1
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")

@app.route("/custom", methods=["POST"])
def custom():
    session["count"] += int(request.form["customnum"])-1
    session["actualcount"] -= 1
    return redirect("/")

@app.route("/")
def indexget():
    if "count" not in session:
        session["count"] = 0
    if "actualcount" not in session:
        session["actualcount"] = 0
    print(session)
    session["count"] += 1
    session["actualcount"] += 1
    return render_template("index.html")

@app.route("/murder_session")
def MURDER_SESSION():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)