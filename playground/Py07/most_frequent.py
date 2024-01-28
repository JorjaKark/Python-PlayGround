def most_frequent(alist):
    dicionario = {}
    novo = []
    for number in alist:
        if number in dicionario:
            dicionario[number] += 1
        else:
            dicionario[number] = 1
    
    maxima_frequencia = max(dicionario.values())

    for key, value in dicionario.items():
        if value == maxima_frequencia:
            novo.append(key)

    if len(novo)>1:
        return max(novo)
    else:
        return novo[0]
