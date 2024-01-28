def count_chars(a_string):
    empty_tuple = ()
    letra = 0
    número = 0
    special = 0
    for n in a_string:
        if n.isalpha():
            letra +=1
        elif n.isnumeric():
            número += 1
        else:
            special +=1

    return (letra, número, special)
