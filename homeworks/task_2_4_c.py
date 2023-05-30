def remove_word_with_one_em(s):
    res = []
    words = s.split()
    for word in words:
        if word.count("!") != 1:
            res.append(word)

    return ' '.join(res)


assert remove_word_with_one_em("Hi!") == ""
assert remove_word_with_one_em("Hi! Hi!") == ""
assert remove_word_with_one_em("Hi! Hi! Hi!") == ""
assert remove_word_with_one_em("Hi Hi! Hi!") == "Hi"
assert remove_word_with_one_em("Hi! !Hi Hi!") == ""
assert remove_word_with_one_em("Hi! Hi!! Hi!") == "Hi!!"
assert remove_word_with_one_em("Hi! !Hi! Hi!") == "!Hi!"