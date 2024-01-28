def academy_awards(alist):
    awards_count = {}

    for category, movie in alist:
        if movie in awards_count:
            awards_count[movie] += 1
        else:
            awards_count[movie] = 1

    return awards_count
