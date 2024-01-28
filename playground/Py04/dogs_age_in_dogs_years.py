def dogs(h_age):
    d_age = 0
    if h_age == 1 or h_age == 2:
        d_age = h_age * 10.5
    else:
        d_age = 21.0 + (h_age - 2) * 4
    return d_age
