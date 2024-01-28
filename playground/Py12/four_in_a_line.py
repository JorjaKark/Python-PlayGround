def four_in_line(board):
    flag = False
    for n in range(len(board)):
        red_acc = 0
        yellow_acc = 0
        for i in range(len(board[0])):
            if board[n][i] == 1:
                red_acc += 1
            elif board[n][i] == 2:
                yellow_acc += 1
            if red_acc == 4 or yellow_acc == 4:
                #red ou amarelo ganham
                flag = True
                return {(n,i-3), (n,i)}
 # lines vertical ou diagonal
    if flag == False:
        list_yellow = []
        list_red = []
        dict_coordinates = {"yellow": [], "red": [] }
        for n in range(len(board)):
            for i in range(len(board[0])):
                if board[n][i] == 1:

                    dict_coordinates["red"].append((n,i))
                elif board[n][i] == 2:
 
                    dict_coordinates["yellow"].append((n,i))
        
        list_yellow.append(dict_coordinates.get("yellow"))
        list_yellow = list_yellow[0]
        list_red.append(dict_coordinates.get("red"))
        list_red = list_red[0]
        #diagonal
        if flag == False:
            sorted(list_yellow)
            acc_diagonal_direita = 0
            acc_diagonal_esquerda = 0

            for index in range(len(list_yellow)):
                
                nd = list_yellow[index][0]
                id = list_yellow[index][1]

                ne = list_yellow[index][0]
                ie = list_yellow[index][1]
                a = index + 1
                for n_next,i_next in list_yellow[a:]:
                    if n_next == (nd + 1) and i_next == (id + 1):
                        acc_diagonal_direita += 1
                    
                        nd += 1
                        id += 1
                    elif n_next == (ne + 1) and i_next == (ie - 1):
                        acc_diagonal_esquerda += 1
                        ne += 1
                        ie -= 1
                    if acc_diagonal_direita >= 3:
                        flag = True
                        return {(n_next, i_next),(n_next - 3, i_next - 3)}
                    elif acc_diagonal_esquerda >= 3:
                        flag = True
                        return {(n_next, i_next),(n_next - 3, i_next + 3)}
                         
                if not flag:
                    for index in range(len(list_yellow)):
                        n = list_yellow[index][0]
                        i = list_yellow[index][1]
                        a = index + 1
                        acc_vertical = 0
                        for n_next,i_next in list_yellow[a:]:
                            if n_next == (n + 1) and i_next == i:
                                acc_vertical += 1
                                n += 1
                            if acc_vertical >= 3:
                                flag = True
                                return {(n_next, i_next),(n_next - 3, i_next)}    
        if flag == False:
            sorted(list_red)
            acc_diagonal_direita = 0
            acc_diagonal_esquerda = 0
            for index in range(len(list_red)):
                nd = list_red[index][0]
                id = list_red[index][1]
                ne = list_red[index][0]
                ie = list_red[index][1]
                a = index + 1
                for n_next,i_next in list_red[a:]:
                    if n_next == (nd + 1) and i_next == (id + 1):
                        acc_diagonal_direita += 1
                        nd += 1
                        id += 1

                    elif n_next == (ne + 1) and i_next == (ie - 1):
                        acc_diagonal_esquerda += 1
                        ne += 1
                        ie -= 1
                    if acc_diagonal_direita >= 3:
                        flag = True
                        return {(n_next, i_next),(n_next - 3, i_next - 3)}
                    elif acc_diagonal_esquerda >= 3:
                        flag = True
                        return {(n_next, i_next),(n_next - 3, i_next + 3)}       
                if not flag:
                    for index in range(len(list_red)):
                        n = list_red[index][0]
                        i = list_red[index][1]
                        a = index + 1
                        acc_vertical = 0
                        for n_next,i_next in list_red[a:]:
                            if n_next == (n + 1) and i_next == i:
                                acc_vertical += 1
                                n += 1
                            if acc_vertical >= 3:
                                flag = True
                                return {(n_next, i_next),(n_next - 3, i_next)}
