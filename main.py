from flask import Flask, render_template, request, session
import random
import os

app = Flask(
    __name__,
    template_folder=os.path.abspath('.'),
    static_folder=os.path.abspath('.')
)

app.secret_key = "secret_key_for_session"

win_rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def initialize_score():
    if "user_score" not in session:
        session["user_score"] = 0
    if "computer_score" not in session:
        session["computer_score"] = 0

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "Tie"
    elif win_rules[user] == computer:
        return "User"
    else:
        return "Computer"

@app.route("/", methods=["GET", "POST"])
def home():
    initialize_score()

    result = ""
    user_choice = ""
    computer_choice = ""

    if request.method == "POST":

        if request.form.get("reset"):
            session["user_score"] = 0
            session["computer_score"] = 0
            result = "Score Reset!"
        else:
            user_choice = request.form.get("choice")
            computer_choice = get_computer_choice()

            winner = decide_winner(user_choice, computer_choice)

            if winner == "User":
                session["user_score"] += 1
                result = "You Win!"
            elif winner == "Computer":
                session["computer_score"] += 1
                result = "Computer Wins!"
            else:
                result = "It's a Tie!"

    return render_template(
        "index.html",
        result=result,
        user_choice=user_choice,
        computer_choice=computer_choice,
        user_score=session["user_score"],
        computer_score=session["computer_score"]
    )

if __name__ == "__main__":
    app.run(debug=True)