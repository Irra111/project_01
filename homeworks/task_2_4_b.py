def remove_last_em(s):
    if s.endswith("!"):
        s = s[:-1]

    return s


assert remove_last_em("Hi!") == "Hi"
assert remove_last_em("Hi!!!") == "Hi!!"
assert remove_last_em("!Hi") == "!Hi"