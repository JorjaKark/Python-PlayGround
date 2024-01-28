def get_positions(sentence, word_list):
    sentence = sentence.split()
    positions = ''
    for word in sentence:
        for x in word_list:
            if word == x:
                index= str(word_list.index(x))
                positions+=index
    
    if len(positions)<2:
        return ""
    
    return " ".join(positions)
