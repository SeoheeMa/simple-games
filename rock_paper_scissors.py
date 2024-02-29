import random


def get_computer_choice():
    options_list = ["Rock", "Paper", "Scissors"]
    i = random.randint(0, 2)
    return options_list[i]


def get_player_choice():
    while True:
        try:
            choice = input("Choose rock, paper, scissors: ").capitalize()
            if (choice == "Rock") or (choice == "Paper") or (choice == "Scissors"):
                return choice
            else:
                print("Rock, paper, scissors?")
        except ValueError:
            print("Invalid input.")


def play_game():
    computer = get_computer_choice()
    player = get_player_choice()

    print(f"Computer: {computer}, Player: {player}")

    if computer == player:
        print("It's a tie!")
        return "tie"

    elif (computer == "Rock" and player == "Paper") or (computer == "Paper" and player == "Scissors") or (
            computer == "Scissors" and player == "Rock"):
        print("You win!")
        return "win"
    else:
        print("You lose!")
        return "lose"


def play_again():
    while True:
        replay = input("Do you want to play again (Y/N)? ").upper()

        if replay == "Y":
            print("Alright. Let's play again!")
            return True
        elif replay == "N":
            print("--- Game ended ---")
            return False
        else:
            print("Choose Y or N.")


def get_stats(tie, player_win, player_lose):
    result = play_game()

    if result == "tie":
        tie += 1
    elif result == "win":
        player_win += 1
    else:
        player_lose += 1

    return tie, player_win, player_lose


def main():
    play = True
    round_num = 1
    tie, player_win, player_lose = 0, 0, 0

    while play:
        print(f"--- Round {round_num} ---")
        tie, player_win, player_lose = get_stats(tie, player_win, player_lose)
        play = play_again()
        if not play:
            print(f"Tie: {tie}, Player win: {
                  player_win}, Player lose: {player_lose}")
        else:
            round_num += 1


if __name__ == "__main__":
    main()
