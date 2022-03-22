def rook_moves(pos):
    pos_m = pos%8
    if pos_m == 0:
        pos_m = 8
    pos_f = pos//8
#    if pos_f == 0:
#        pos_f = 8
    l_horizontal = []
    l_vertical = []
    for p in range(-(pos_m)+1,8-pos_m+1):
        l_horizontal.append(pos+p)
        
    for p in range(-(pos_f), -(pos_f)+9 ):
        l_vertical.extend([p*8+pos])
        
    l_horizontal.append(1)
    l_vertical.append(1)
    l = [l_horizontal, l_vertical]
    return(l)
        
if __name__ == "__main__":
    print(rook_moves(1))