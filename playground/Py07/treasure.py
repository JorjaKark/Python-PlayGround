def treasure(clues, current_location=(0, 0)):
    if current_location not in clues:
        return current_location
    else:
        next_location = clues[current_location]
        del clues[current_location] 
        return treasure(clues, next_location)
