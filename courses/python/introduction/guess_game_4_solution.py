import random

# Set the secret number to be a random number between 1 and 99 inclusive
secret_number = random.randint(1, 99)
# Set the guess to be 0 so it is defined
guess = 0
# Set the guess counter to be 0
guess_counter = 0

while guess != secret_number:
    # Ask the user to enter their secret number and convert it to an integer using int
    guess = int(input("Guess the secret number: "))

    if guess < secret_number:
        print("Wrong, the secret number is higher")
    elif guess > secret_number:
        print("Wrong, the secret number is lower")

    guess_counter = guess_counter + 1

    if guess_counter == 3:
        break

if guess == secret_number:
    print("You guessed correctly, 100 points!")
else:
    # Score is 100 - the distance of the guess from the secret_number
    score = 100 - abs(secret_number - guess)
    print("You have reached your maximum number of guesses!")
    print("The answer was " + str(secret_number) + " you get " + str(score) + " points!")
