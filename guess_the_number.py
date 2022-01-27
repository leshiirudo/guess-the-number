import random

# welcome message
print("Welcome to Guess the Number!" + "\n")

# select difficulty
while True:
    difficulty = input("Select difficulty (Easy, Normal, Hard): ")
    difficulty = difficulty.lower()
    if difficulty == "easy":
        max_guess = 20
        print()
        break
    elif difficulty == "normal":
        max_guess = 100
        print()
        break
    elif difficulty == "hard":
        max_guess = 500
        print()
        break
    else:
        print("Please select an existing difficulty.")

# initiate game
number_to_guess = random.randint(1, max_guess)
number_of_guesses = 1

# run game
while True:
    player_guess = 0
    try:
        player_guess = int(input("Guess a number between 1 and " + str(max_guess) + ": "))
    except ValueError:
        print("This isn't a number. Game over.")
        break
    if player_guess == number_to_guess:
        print("\n" + "Congrats! You won in " + str(number_of_guesses) + " tries! Game over.")
        break
    elif player_guess < number_to_guess:
        print("This number is too low! Try higher.")
        number_of_guesses += 1
    elif player_guess > number_to_guess:
        print("This number is too big! Try lower.")
        number_of_guesses += 1