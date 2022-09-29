import random
import os

magicNumber = random.randint(1, 10)

guesses = 1
guessRemaining = 3

judged = False

def judgeDredd(guessesRemaining):
    global judged
    if guessesRemaining == 0:
        os.system('clear')
        print("You're all out of guesses! Better luck next time")
        judged = True
        return judged
    else:
        pass

def evalGuess(guess):
    global guessRemaining
    global guesses

    if guess > magicNumber:
        guessRemaining = guessRemaining - 1
        input(f"You're a little high.\n{guessRemaining} guesses remaining\n\nPress any key to try again.")
        guesses = guesses + 1
        wagerAGuess()
    elif guess < magicNumber:
        guessRemaining = guessRemaining - 1
        input(f"You're a little low.\n{guessRemaining} guesses remaining\n\nPress any key to try again.")
        guesses = guesses + 1
        wagerAGuess()
    elif guess == magicNumber:
        print(f"\nCorrect! The magic number was {magicNumber}, "
              f"and your guess was {guess}."
              f"\n========================================================\n"
              f"Guesses attempted: {guesses}\nGuesses remaining {guessRemaining}")
        exit()

def wagerAGuess():
    global guessRemaining

    os.system('clear')
    judgeDredd(guessRemaining)
    if not judged:
        guess = int(input("What's the magic number?: "))
        evalGuess(guess)
    elif judged:
        pass

if __name__ == "__main__":
    wagerAGuess()
