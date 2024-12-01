"""
    Useful Functions for modelling game of life
"""
pdv_blue = 100
pdv_red = 100

def perte_hp(a):
    """Modelling the lost of hp

    Args:
        a (_integer_): _1 for player blue, 2 for player red_
    """
    global pdv_blue,pdv_red
    if a == 1 :
        pdv_blue -= 1
    else : 
        pdv_red -= 1


def survival(x, y, universe):
    """Evolution of a cell in a given universe
    universe[x][y] == 1 : Team blue
    universe[x][y] ==2 : Team red

    Args:
        x (_integer_): _x position_
        y (_integer_): _y position_
        universe (_list_)

    Returns:
        _integer_: _characterize if a cell from a player is alive or not_
    """
    
    a, b = len(universe), len(universe[0])
    nb_vivant = 0
    #Coding of the base for each player (y==0 and y == b-1)
    if (y == 0 or y == b-1) and universe[x][y] != 0 :
        if universe[x][y] == 2 and y == 0 :    
            perte_hp(1)
        elif universe[x][y] == 1 and y == b-1  :
            perte_hp(2)
        return 0
    #Add the information of the neighbourhood of a cell
    #If the cell comes from a different team  -1 for nb_vivant (malus)
    else: 
        if universe[x][y] == 1:#Team blue
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    ni, nj = (i % a), (j % b)
                    if universe[ni][nj] != 2 :
                        nb_vivant += universe[ni][nj]
                    else : 
                        nb_vivant -= 1
            nb_vivant -= universe[x][y]

            if nb_vivant == 3:
                return 1
            elif nb_vivant < 2 or nb_vivant > 3:
                return 0
            else:
                return universe[x][y]
        if universe[x][y] == 2 :#Team red
            for i in range(x-1, x+2):
                    for j in range(y-1, y+2):
                        ni, nj = (i % a), (j % b)
                        if universe[ni][nj] != 2 :
                            nb_vivant -= universe[ni][nj]
                        else : 
                            nb_vivant += 1
            
            nb_vivant -= 1
            if nb_vivant == 3:
                return 2
            elif nb_vivant < 2 or nb_vivant > 3:
                return 0
            else:
                return universe[x][y]
        if universe[x][y] == 0:#The cell doesn't belong to any team
            nb_2 = 0
            nb_1 = 0
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    ni, nj = (i % a), (j % b)
                    if universe[ni][nj] == 1 : 
                        nb_1 += 1
                    elif universe[ni][nj] == 2 : 
                        nb_2 += 1
            nb_vivant = max(nb_1-nb_2,nb_2-nb_1)
            if nb_1-nb_2 >= 0 : 
                if nb_vivant == 3:
                    return 1
                elif nb_vivant < 2 or nb_vivant > 3:
                    return 0
                else:
                    return universe[x][y]
            else : 
                if nb_vivant == 3:
                    return 2
                elif nb_vivant < 2 or nb_vivant > 3:
                    return 0
                else:
                    return universe[x][y]
                
def refresh(universe):
    """_create new universe_

    Args:
        universe (_list_)

    Returns:
        _list_: _universe_
    """
    a, b = len(universe), len(universe[0])
    new_universe = [[0 for i in range(b)] for j in range(a)]
    for i in range(a):
        for j in range(b):
            new_universe[i][j] = survival(i, j, universe)
    return new_universe

def add_seed_to_universe(seed,universe,x,y):
    """"
    Args:
        seed (_list_): _description_
        universe (_list_): _description_
        x (_integer_): _position x_
        y (_integer_): _position y_

    Returns:
        _type_: _description_
    """
    for i in range(len(seed)):
        for j in range(len(seed[0])):
            universe[(i-len(seed)//2+x)%len(universe)][(j-len(seed[0])//2+y)%len(universe[0])] = seed[i][j]
    return universe