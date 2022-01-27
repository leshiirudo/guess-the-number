import random

print("Welcome to Guess the Number!")
print()

difficulty_selected = False # using boolean to end loop when difficulty was chosen

while difficulty_selected == False:
    difficulty = input("Select difficulty (Easy, Normal, Hard): ")
    difficulty.lower()
    if difficulty == "easy":
        max_guess = 20
        difficulty_selected = True
    elif difficulty == "normal":
        max_guess = 100
        difficulty_selected = True
    elif difficulty == "hard":
        max_guess = 1000
        difficulty_selected = True
    else:
        print("Please select an existing difficulty.")

print()

number_to_guess = random.randint(1, max_guess)
number_of_guesses = 1
game_in_progress = True # using boolean to check if game is still in progress

while game_in_progress == True:
    player_guess = 0
    try:
        player_guess = int(input("Guess a number between 1 and " + str(max_guess) + ": "))
    except ValueError:
        print("This isn't a number.")
        game_in_progress = False # trying to figure out how to go back to start of loop to avoid game over
    if player_guess == number_to_guess:
        print()
        print("Congrats! You won in " + str(number_of_guesses) + " tries!")
        break
    elif player_guess < number_to_guess:
        print("This number is too low! Try higher.")
        number_of_guesses = number_of_guesses + 1
    elif player_guess > number_to_guess:
        print("This number is too big! Try lower.")
        number_of_guesses = number_of_guesses + 1

print()
print("Game over.")