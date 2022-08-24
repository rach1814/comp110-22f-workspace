"""an example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1 and 5. What is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET: 
    print("you guessed correctly!!!")
    print("have a wonderful day!")
else:
    print("sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("you guessed too high")
    else:
        print("you guessed too low!")

print("game over.")
