def map(pos, steps):
    steps = steps.split("-")
    pos = list(pos)
    print(steps)
    for step in steps:
        if step == "up":
            pos[1] += 1
        elif step == "down":
            pos[1] -= 1  
        elif step == "right":
            pos[0] += 1
        elif step == "left":
            pos[0] -= 1

    pos = tuple(pos)
    return pos

