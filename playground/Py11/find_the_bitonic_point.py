def bitonic_point(f):
    result = f()
    for a in range(0, len(result)+1):
        b = a + 1
        if result[a] > result[b]:
            return result[a]

