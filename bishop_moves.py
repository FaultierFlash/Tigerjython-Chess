def bishop_moves(pos):
    
    pos_m = pos%8
    if pos_m == 0:
        pos_m = 8
        
    l1 = []
    l2 = []
    
    for p in range(-pos_m+1, 9-pos_m):
        l1.append(pos+8*p+p)
        
    for p in range(-(8-pos_m), pos_m):  
        l2.append(pos+8*p-p)
        
    l1.append(1)
    l2.append(1)
    
    l3 = [l1, l2]
    
    return(l3)
        


if __name__ == '__main__':
    print(bishop_moves(11))