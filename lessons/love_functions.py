"""some tender loving functions"""

def love(subject: str) -> str:
    """given a subject as a parameter, returns a loving string"""
    return f"i love you {subject}!"

def spread_love(to: str, num: int) -> str:
    """generates a str repeating a loving message n times """
    love_note: str = ""
    how_much: int = 0

    while how_much < num:
        love_note += love(to) + "\n"
        how_much +=1

    return love_note

print(spread_love("rachel", 3))




