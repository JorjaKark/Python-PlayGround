def bagdiff(xs, ys):
    for numbers in xs:
        for elimination in ys:
            if numbers == elimination:
                xs.remove(numbers)
            else:
                pass

    return xs
