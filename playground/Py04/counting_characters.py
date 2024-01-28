def count_chars(astring, character):
    x = 0
    counter = 0
    for c in astring:
        if c == character:
            counter += 1
    if counter == 0:
        counter = -1
    return counter
