def remove_exclamation_marks(s):
    return s.replace("!", "")


assert remove_exclamation_marks("Hi! Hello!") == "Hi Hello"
assert remove_exclamation_marks("") == ""
assert remove_exclamation_marks("Oh, no!!!") == "Oh, no"