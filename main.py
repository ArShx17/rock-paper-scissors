from flask import Flask, render_template, request
import random
import os

app = Flask(
    __name__,
    template_folder=os.path.abspath('.'),
    static_folder=os.path.abspath('.')
)

win_rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    user_choice = ""
    computer_choice = ""

    if request.method == "POST":
        user_choice = request.form.get("choice")
        computer_choice = random.choice(["rock", "paper", "scissors"])

        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif win_rules[user_choice] == computer_choice:
            result = "You Win!"
        else:
            result = "Computer Wins!"
    return render_template(
        "index.html",
        result=result,
        user_choice=user_choice,
        computer_choice=computer_choice
    )

if __name__ == "__main__":
    app.run(debug=True)
