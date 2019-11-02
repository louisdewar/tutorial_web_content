# Set the secret number to be 5
secret_number = 5
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
    print("You guessed correctly, welcome to the secret area!")
else:
    print("You have reached your maximum number of guesses!")
