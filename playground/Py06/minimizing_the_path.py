def min_path(path):
    lista_de_pares = []
    final_list = []
    for instructions in path:
        lista_de_pares.append(instructions)
        if "DOWN" in lista_de_pares and "UP" in lista_de_pares:
            lista_de_pares.remove("DOWN")
            lista_de_pares.remove("UP")
        elif "RIGHT" in lista_de_pares and "LEFT" in lista_de_pares:
            lista_de_pares.remove("RIGHT")
            lista_de_pares.remove("LEFT")
    if lista_de_pares == []:
        return path

    for instructions in path:
        for elements in lista_de_pares:
            if instructions == elements:
                final_list.append(instructions)
                lista_de_pares.remove(instructions)

    return final_list
