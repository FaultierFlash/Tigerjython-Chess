def pawn_moves(pos, moved, color):
    
    pos_m = pos%8
    
    l = []
    
    if color:
        if not moved:
            l = [[pos-8, pos-16, 0]]
        else:
            l = [[pos - 8, 0]]
            
        if pos_m == 1:
            l.append([pos-9, 2])
            
        elif pos_m == 0:
            l.append([pos-7, 2])
            
        else:
            l.extend([[pos-9, 2], [pos-7, 2]])
            
    else:
        if not moved:
            l = [[pos+8, pos+16, 0]]
        else:
            l = [[pos + 8, 0]]
            
        if pos_m == 1:
            l.append([pos+9, 2])
            
        elif pos_m == 0:
            l.append([pos+7, 2])
            
        else:
            l.extend([[pos+9, 2], [pos+7, 2]])
        
    return(l)


if __name__ == '__main__':
    print(pawn_moves(16, True, color = False))

