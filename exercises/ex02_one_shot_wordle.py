"""EX02- wordle with one shot at guessing. """
__author__ = "730334012"

# white, green and yellow emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"
user_guess: str = input(f"What is your {len(secret_word)} letter guess? ")
while len(user_guess) != len(secret_word):
    user_guess: str = input(f"That was not {len(secret_word)} letters, try again ")

i: int = 0
emojified: str = ""

while i < len(secret_word):
    if user_guess[i] == secret_word[i]:
        emojified += GREEN_BOX
    else:
        j: int = 0
        found: bool = False
        while found is False and j < len(secret_word):
            if user_guess[i] == secret_word[j]:
                found = True
            else:
                j += 1
        if found is True:
            emojified += YELLOW_BOX
        else:
            emojified += WHITE_BOX
    i += 1

if user_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")

print(emojified)