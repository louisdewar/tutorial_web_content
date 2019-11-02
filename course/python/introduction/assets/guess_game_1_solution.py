# Set the secret number to be 5
secret_number = 5

# Ask the user to enter their secret number and convert it to an integer using int
guess = int(input("Guess the secret number: "))

if guess == secret_number:
    print("You guessed correctly, welcome to the secret area!")
elif guess < secret_number:
    print("Wrong, the secret number is higher")
# We've already checked if the number is equal or higher, the only thing left is if the secret number is lower
else:
    print("Wrong, the secret number is lower")
