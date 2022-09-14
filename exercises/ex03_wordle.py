"""ex03 Structured Wordle."""
__author__ = "730334012"


def contains_char(ss: str, sc: str) -> bool:  # ss is the string that is being searched through, sc is the single character that we are looking for
    """When given two strings, will search through the first for single character (second string) and will return true if character is found."""
    assert len(sc) == 1
    i: int = 0  # index tracker
    while i < len(ss):
        if ss[i] == sc:
            return True
        i = i + 1
    return False


# white, green and yellow emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """When given two strings of equal length (a guess and a secret), it will return colored emojis based on matching characters in the guess and the secret."""
    assert len(guess) == len(secret)  # the guess must be the same length as the secret
    i: int = 0  # index tracker
    es: str = ""

    while i < len(guess):
        if guess[i] == secret[i]:
            es += GREEN_BOX
            i = i + 1
        elif contains_char(secret, guess[i]) is True:
            es += YELLOW_BOX
            i = i + 1
        else:
            es += WHITE_BOX
            i = i + 1
    return es


def input_guess(expected_length: int) -> str:
    """When given an expected length of a guess, will prompt the user for a guess until they guess a word of the expected length."""
    user_guess: str = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length:
        user_guess: str = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""  # establish what secret word is as a variable, keep track of how many turns user has spent, whether user has won game, & control flow of game.
    secret: str = "codes"
    expected_length: int = len(secret)
    user_guess: str = ""
    turns: int = 1

    while turns <= 6 and user_guess != secret:
        print(f"=== Turn {turns}/6 === ")
        user_guess = input_guess(expected_length)
        print(emojified(user_guess, secret))
        if user_guess == secret:
            print(f"You won in {turns}/6 turns! ")
        elif turns == 6:
            print("X/6 - Sorry, try again tomorrow!")
        turns = turns + 1
    

if __name__ == "__main__":
    main()