def king_moves(pos, moved):
    
    pos_m = pos%8
    if pos_m == 0:
        pos_m = 8
        
    l1 = [[pos+8, 1], [pos-8, 1]]
    l2 = []
    
    #if not moved:
         
    
    if pos_m >= 2:
        l1.extend([[pos+7, 1], [pos-1, 1], [pos-9, 1]])
        
    if pos_m <= 6:
        l1.extend([[pos-7, 1], [pos+1, 1], [pos+9, 1]])
        
    for i in l1:
        if i[0] >= 0 and not i[0] > 64:
            l2.append(i)
        
    return(l2)
        
    
if __name__ == '__main__':
    print(king_moves(1))
