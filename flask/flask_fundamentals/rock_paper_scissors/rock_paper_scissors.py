from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/result", methods=["POST"])
def result():
    choice = request.form["choice"]
    import random
    computerchoice = random.choice(["rock", "paper", "scissors"])
    def isWin(choice,p2):
        if choice == p2:
            return "It's a Tie!"
        winCon = { 
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper",
        }
        if winCon[choice] == p2:
            return "You Win"
        return "You Lose"
    final = isWin(choice,computerchoice)
    return render_template("result.html", choice=choice, whatever=final, computerchoice = computerchoice)

if __name__ == "__main__":
    app.run(debug=True)