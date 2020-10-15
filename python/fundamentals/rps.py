def isWin(p1,p2):
    if p1 == p2:
        return "Tie"
    winCon = { 
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }
    if winCon[p1] == p2:
        return "Win"
    return "Lose"
print(isWin("rock","paper"))