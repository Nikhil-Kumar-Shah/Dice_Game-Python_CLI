import random


def dice_roll():
    return random.randint(1, 6)


print("🎲 Welcome to the Dice Game!")

while True:
    user_score = 0
    computer_score = 0
    user_total = 0
    computer_total = 0

    user_name = input("Enter your name: ")

    rounds = int(input("How many rounds do you want to play? "))
    print("===========================")
    print("⭐", user_name, "vs 💻 Computer — Best of", rounds, "rounds!")
    print("===========================")

    for i in range(1, rounds + 1):
        print("🔷 Round", i)
        user_roll = dice_roll()
        computer_roll = dice_roll()

        print("🎲", user_name, "rolled:", user_roll)
        print("🎲 Computer rolled:", computer_roll)

        if user_roll > computer_roll:
            print("✅", user_name, "wins this round!")
            user_score = user_score + 1
            user_total = user_total + user_roll
        elif computer_roll > user_roll:
            print("❌ Computer wins this round!")
            computer_score = computer_score + 1
            computer_total = computer_total + computer_roll
        else:
            print("🤝 This round is a tie!")
        print("===========================")

    print("🏁 Game Over!")
    print("===========================")
    print("⭐", user_name, "total wins:", user_score)
    print("⭐", user_name, "total score:", user_total)
    print("===========================")
    print("💻 Computer total wins:", computer_score)
    print("💻 Computer total score:", computer_total)
    print("===========================")

    if user_score > computer_score:
        print("🎉 Congratulations", user_name, "you win the game! 🎉")
    elif computer_score > user_score:
        print("💻 Computer wins the game! Better luck next time!")
    else:
        print("🤝 It's a draw! Well played both!")
    print("===========================")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        print("👋 Thanks for playing! Goodbye.")
        break
