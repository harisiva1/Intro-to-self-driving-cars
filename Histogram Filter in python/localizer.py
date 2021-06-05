#import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs


def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    pre =[]
    
    
    for i in range(len(beliefs)):
        row =[]
        for j in range(len(beliefs[0])):            
            if (grid[i][j] == color):
                row.append(beliefs[i][j] * p_hit)                                
            else:
                row.append(beliefs[i][j] * p_miss)
        pre.append(row)
                
        
    #print(pre)
    
    s = []
    for i in range(len(pre)):
        a = sum(pre[i])
        s.append(a)
    print(s)
    
    for i in range(len(pre)):
        col =[]
        for j in range(len(pre[0])):
            col.append(pre[i][j] /sum(s))
        new_beliefs.append(col)
    
    #print(new_beliefs)
    return new_beliefs


    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        new_i = 0
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = beliefs[i][j]
    return blur(new_G, blurring)