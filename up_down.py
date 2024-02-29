import random


def get_user_input():
    while True:
        try:
            num = int(input("Guess a number between 1 and 100: "))
            if 1 <= num <= 100:
                return num
            else:
                print("The number should be between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def up_down(target_num):
    count = 0

    while True:
        count += 1
        num = get_user_input()

        if num < target_num:
            print("Up")
        elif num > target_num:
            print("Down")
        else:
            print("You are correct!")
            print("Attempts tried:", count)
            return count


def play_again():
    while True:
        try:
            replay = input("Do you want to play again (Y/N)? ").upper()

            if replay == "Y":
                print("Alright. Let's play again!")
                return True
            elif replay == "N":
                print("--- Game ended ---")
                return False
            else:
                print("Choose Y or N.")
        except ValueError:
            print("Invalid input.")


def main():
    play = True
    round_num = 1
    count = 0

    while play:
        target_num = random.randint(1, 100)

        print(f"--- Round {round_num} ---")
        print(f"Previous max attempts: {count}")
        count = up_down(target_num)
        play = play_again()
        round_num += 1


if __name__ == "__main__":
    main()
