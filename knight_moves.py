def knight_moves(pos):
    pos_m = pos%8
    if pos_m == 0:
        pos_m = 8

    l1 = []
    l2 = []
       
    if pos_m >= 2:
        l1.extend([[pos+16-1, 1], [pos-16-1, 1]])
        if pos_m >= 3:
            l1.extend([[pos+8-2, 1],[pos-8-2, 1]])
            
    if pos_m <= 7:
        l1.extend([[pos+16+1, 1],[pos-16+1, 1]])
        if pos_m <= 6:
            l1.extend([[pos+8+2, 1],[pos-8+2, 1]])
    
    for i in l1:
        if i[0] >= 0 and not i[0] > 64:
            l2.append(i)
        
    return(l2)
    
if __name__ == '__main__':
    print(knight_moves(64))
