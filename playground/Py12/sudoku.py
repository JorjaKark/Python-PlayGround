def solve_sudoku(board):
    board_dict = {key_board: board[key_board] for key_board in range(0,9)}
    #print(board_dict)
    colunas_dict = {key_colunas: [board[linhas4][key_colunas] for linhas4 in range(0,9)] for key_colunas in range(0,9)}
    nenhum_zero= {}
    um_zero = {}
    dois_zeros = {}
    for key, value in board_dict.items():
        count_0 = value.count(0)
        if count_0 == 0:
            nenhum_zero[key] = value
        elif count_0 == 1:
            um_zero[key] = value
        elif count_0 == 2:
            dois_zeros[key] = value
    
    for key2, value2 in um_zero.items():
        for number1 in range(1,10):
            if number1 not in value2:
                um_zero[key2] = [number1 if x== 0 else x for x in value2]
                for key_b in board_dict.keys():
                    if key_b == key2:
                        board_dict[key_b] = um_zero[key2]

    coordenadas_zeros = []
    for linha_index,value3 in dois_zeros.items():
       
        for coluna_index, number2 in enumerate(value3):
            if number2 == 0:
                coordenadas_zeros.append((linha_index, coluna_index))
    
    colunas_dict2 = {}
    for zero in coordenadas_zeros:
        colunas_dict2[zero[1]] = colunas_dict.get(zero[1])

    #print("colunas dict", colunas_dict2)
    #print(coordenadas_zeros)
    coord_1 = [v[1] for v in coordenadas_zeros]
    #print("coord_1 ", coord_1)
    for ind, coord in enumerate(coordenadas_zeros):
     #   print(coord)
        
        for n in range(1, 10):
            if n not in colunas_dict2.get(coord_1[ind]):
                board_dict[coord[0]][coord[1]] = n
                
                break
    return list(board_dict.values())
