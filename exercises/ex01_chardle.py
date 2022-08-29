"""EX01 - Chardle: a cute step towards Wordle."""
__author__ = "730334012"

user_word: str = input("Enter a 5-character word: ")
if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

user_character: str = input("Enter a single character: ")
if len(user_character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + user_character + " in " + user_word)


character_counter = 0

if user_character == user_word[0]:
    print(user_character + " found at index 0")
    character_counter = character_counter + 1

if user_character == user_word[1]:
    print(user_character + " found at index 1")
    character_counter = character_counter + 1

if user_character == user_word[2]:
    print(user_character + " found at index 2")
    character_counter = character_counter + 1

if user_character == user_word[3]:
    print(user_character + " found at index 3")
    character_counter = character_counter + 1

if user_character == user_word[4]:
    print(user_character + " found at index 4")
    character_counter = character_counter + 1


if character_counter == 0:
    print("No instances of " + user_character + " found in " + user_word)

if character_counter == 1:
    print(str(character_counter) + " instance of " + user_character + " found in " + user_word)

if character_counter > 1:
    print(str(character_counter) + " instances of " + user_character + " found in " + user_word)