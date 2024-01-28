def repeated_letter(s):
    modified_string = []
    repeated_letters = []
    for letter in s:
        if letter not in modified_string:
            modified_string.append(letter)
        else:
            repeated_letters.append(letter)
    if len(repeated_letters) > 1:
        for letter in s:
            if letter in repeated_letters:
                return letter

