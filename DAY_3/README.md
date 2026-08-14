# Guess the Number Game

This is a simple Python mini project where the computer randomly selects a number between 1 and 20, and the player has 6 attempts to guess the correct number.

## Description

The program generates a random number using the `random` module. The user enters a guess, and the program gives a hint whether the guess is too high or too low. The game ends when the correct number is guessed or all 6 attempts are used.

## Concepts Used

- Python `random` module
- `randint()`
- `for` loop
- `range()`
- `if-elif-else`
- `break` statement
- `input()`
- Type conversion using `int()`
- String concatenation

## Program Code

    import random

    secret_number = random.randint(1, 20)

    print('I am thinking of a number between 1 and 20.')

    for guesses_taken in range(1, 7):
        print('Take a guess.')
        guess = int(input('>'))

        if guess < secret_number:
            print('Your guess is too low.')

        elif guess > secret_number:
            print('Your guess is too high.')

        else:
            break

    if guess == secret_number:
        print('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
    else:
        print('Nope. The number was ' + str(secret_number))

## Execution Flow

    Start
      ↓
    Generate random number between 1 and 20
      ↓
    Allow maximum 6 guesses
      ↓
    Take user input
      ↓
    Compare guess with secret number
      ↓
    Guess is too low → Display "Too low"
      ↓
    Guess is too high → Display "Too high"
      ↓
    Correct guess → break the loop
      ↓
    Display result
      ↓
    End

## Sample Output

    I am thinking of a number between 1 and 20.
    Take a guess.
    >5
    Your guess is too low.
    Take a guess.
    >15
    Your guess is too high.
    Take a guess.
    >10
    Your guess is too high.
    Take a guess.
    >7
    Good job! You got it in 4 guesses!

## How It Works

### Random Number

    secret_number = random.randint(1, 20)

Generates a random integer between 1 and 20.

### Number of Attempts

    for guesses_taken in range(1, 7):

Allows the user to make a maximum of 6 guesses.

### Checking the Guess

If the guess is smaller:

    Your guess is too low.

If the guess is larger:

    Your guess is too high.

If the guess is correct, `break` stops the loop.

## Author

**Sahil Ranade**

AIML Batch