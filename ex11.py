"""
Author -- Atieh yazdani
Matr.Nr -- K11932911
Exercise -- 11

"""

import numpy as np

def __compute_next_state__(state):
    input = np.array(state)
    result = np.zeros(input.shape, dtype=bool)

    for ixr, row in enumerate(state, 1):
        for ixc,col in enumerate(row, 1):
            live_neighbors, dead_neighbors = neighbors(1,ixr,ixc,state)
            if col == True and live_neighbors < 2:
                result[ixr-1][ixc-1] = False
            elif col == True and live_neighbors >=2 and live_neighbors <= 3:
                result[ixr-1][ixc-1] = True
            elif col == True and live_neighbors > 3:
                result[ixr-1][ixc-1] = False
            elif col == False and live_neighbors == 3:
                result[ixr-1][ixc-1] = True
    return result

def neighbors(radius, rowNumber, columnNumber,a):
    raw_neighbors = [
         [
             a[i][j] if  i >= 0 and i < len(a) and j >= 0 and j < len(a[0]) else None
                for j in range(columnNumber-1-radius, columnNumber+radius)
         ]for i in range(rowNumber-1-radius, rowNumber+radius)]

    raw_neighbors = np.array(raw_neighbors).flatten().tolist()
    del raw_neighbors[4]
    raw_neighbors = [item for item in raw_neighbors if item != None]
    live_neighbors = raw_neighbors.count(True)
    dead_neighbors = raw_neighbors.count(False)
    return (live_neighbors, dead_neighbors)

# state = [[False,False,True,False],
#          [False,False,True,False],
#          [False,True,False,True],
#          [False,True,False,True]]
# a = np.array(state).flatten()
# print (state)
# result = __compute_next_state__(state)
# print(result)
