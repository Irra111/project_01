def switch_it_up(number):
    numbers = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    return numbers.get(number)


assert switch_it_up(1) == "One"
assert switch_it_up(3) == "Three"
assert switch_it_up(10000) == None