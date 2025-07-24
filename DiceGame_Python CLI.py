import random  # Import the random module for dice rolls

# Define a function to simulate rolling a six-sided die
def dice_roll():
    return random.randint(1, 6)

print("🎲 Welcome to the Dice Game!")  # Initial welcome message

while True:
    # Initialize scores for each session of the game
    user_score = 0            # Number of rounds won by the user
    computer_score = 0        # Number of rounds won by the computer
    user_total = 0            # Sum of dice rolls by the user
    computer_total = 0        # Sum of dice rolls by the computer

    # Get user's name
    user_name = input("Enter your name: ")

    # Ask how many rounds to play
    rounds = int(input("How many rounds do you want to play? "))
    print("===========================")
    print("⭐", user_name, "vs 💻 Computer — Best of", rounds, "rounds!")
    print("===========================")

    # Play the requested number of rounds
    for i in range(1, rounds + 1):
        print("🔷 Round", i)
        user_roll = dice_roll()            # User's dice roll
        computer_roll = dice_roll()        # Computer's dice roll

        print("🎲", user_name, "rolled:", user_roll)
        print("🎲 Computer rolled:", computer_roll)

        # Determine winner of each round and update scores/totals
        if user_roll > computer_roll:
            print("✅", user_name, "wins this round!")
            user_score += 1
            user_total += user_roll
        elif computer_roll > user_roll:
            print("❌ Computer wins this round!")
            computer_score += 1
            computer_total += computer_roll
        else:
            print("🤝 This round is a tie!")
        print("===========================")

    # Show summary at the end of all rounds
    print("🏁 Game Over!")
    print("===========================")
    print("⭐", user_name, "total wins:", user_score)
    print("⭐", user_name, "total score:", user_total)
    print("===========================")
    print("💻 Computer total wins:", computer_score)
    print("💻 Computer total score:", computer_total)
    print("===========================")

    # Declare overall winner or a draw
    if user_score > computer_score:
        print("🎉 Congratulations", user_name, "you win the game! 🎉")
    elif computer_score > user_score:
        print("💻 Computer wins the game! Better luck next time!")
    else:
        print("🤝 It's a draw! Well played both!")
    print("===========================")

    # Prompt to play again or quit
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        print("👋 Thanks for playing! Goodbye.")
        break  # Exit the while loop and end the program
