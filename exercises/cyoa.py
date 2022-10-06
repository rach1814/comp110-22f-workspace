"""EX06 - Choose your own adventure game."""
__author__ = "730334012"


from random import randint
RAM_CONSTANT = "\U0001F40F"

global player
player: str = ""
global points
points: int = 0


def greet() -> None:
    """Greeting player and explaining game."""
    print(f"Welcome to UNC! As students, we go through a lot. This experience will give you a taste of what it's like to be a Tar Heel {RAM_CONSTANT}.")
    player: str = input("What is your name?")  # Track players name
    print(f"Good luck {player}")


def homework() -> None:  # PROCEDURE
    """Gives player choices to make for doing homework."""
    print(f"Hello {player} , You have chosen to do homework. Oh no! You forgot that you also have to register for classes next semester.")
    print("Would you like to register for classes (+ random amount of points) or study for your COMP 110 quiz (+15 points)?")
    choice: str = input("To register, type R. To study, type S")

    global points
    r1: randint = (9, 18)

    if choice == "R":
        points += r1
        print(f"Congrats {player}, You have registered for classes for next semester.")

    if choice == "S":
        points += 15
        print(f"Nice work, {player}. You feel prepared for your COMP 110 quiz now.")


def walk(p: int) -> int:
    """Gives player choices to make for walking on campus."""
    print(f"Be careful {player}, UNC's campus is a treacherous place to walk.")
    print("Watch out for uneven bricks, athletes on scooters. Dont forget to say hi to the crossing guards!")
    print("Would you like to walk through the quad (+5 points) or walk on South Road (+8 points)?") 
    choice: str = input("To walk through the quad, type Q. To walk on South Road, type S.")

    if choice == "Q":
        p += 5
        print(f"You walked through the quad and saw some friends. You now have {p} points. ")

    if choice == "S":
        p += 8
        print(f"You walked down South Road and said hi to the nice crossing guard. You now have{p} points.")

    return p


def main() -> None:
    """Entrypoint of experience."""
    points: int = 0  # Tracks adventure points

    greet()
    print("Today, you have to walk around campus and find a place to do homework.")
    print("Would you like to walk, do homework, or end this experience?")
    choice: str = input("To do homework, type H. To walk around campus, type W. To end this experience, type E")

    gameloop = True
    while gameloop:
        if choice == "H":
            homework()
            print(f"You have {points} points.")

        if choice == "W":
            walk(points)
            points = walk(points)
            print(f"You have {points} points.")

        if choice == "E":
            print(f"Thanks for playing! You earned {points} points.")
            gameloop = False
            exit()


if __name__ == "__main__":
    main()