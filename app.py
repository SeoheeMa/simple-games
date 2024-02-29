from flask import Flask, render_template, request
import random
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)


# Table
class GameHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_choice = db.Column(db.String, nullable=False)
    computer_choice = db.Column(db.String, nullable=False)
    result = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'Player: {self.player_choice}, Computer: {self.computer_choice}, Result: {self.result}'


with app.app_context():
    db.create_all()


def get_computer_choice():
    options_list = ["Rock", "Paper", "Scissors"]
    i = random.randint(0, 2)
    return options_list[i]


def play_game(computer, player):
    if computer == player:
        return "It's a tie"

    elif (computer == "Rock" and player == "Paper") or (computer == "Paper" and player == "Scissors") or (
            computer == "Scissors" and player == "Rock"):
        return "You win"
    else:
        return "You lose"


# Emoji mappings
emoji_mapping = {
    "Rock": "✊",
    "Paper": "✋",
    "Scissors": "✌️"
}


@app.route('/')
def home():
    computer_choice = get_computer_choice()
    result = "None"
    player_choice = request.args.get("query")

    if player_choice in {"Rock", "Paper", "Scissors"}:
        result = play_game(computer_choice, player_choice)

    game_record = GameHistory(
        computer_choice=computer_choice, player_choice=player_choice, result=result)

    try:
        db.session.add(game_record)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print(f"Database error: {e}")

    computer_emoji = emoji_mapping.get(computer_choice)
    player_emoji = emoji_mapping.get(player_choice)

    all_games = GameHistory.query.all()
    total_win = game_record.query.filter_by(result="You win").count()
    total_lose = game_record.query.filter_by(result="You lose").count()
    total_tie = game_record.query.filter_by(result="It's a tie").count()

    context = {
        "computer": computer_emoji,
        "player": player_emoji,
        "result": result,
        "total_win": total_win,
        "total_lose": total_lose,
        "total_tie": total_tie,
        "all_games": all_games
    }

    return render_template('index.html', data=context)


if __name__ == '__main__':
    app.run(debug=True)
