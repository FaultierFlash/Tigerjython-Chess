from copy import deepcopy
raw_moves = [[1, 2, 3, 4, 5, 6, 7, 8, 1], [6, 14, 22, 30, 38, 46, 54, 62, 1], [-39, -30, -21, -12, -3, 6, 15, 24, 1], [-8, -1, 6, 13, 20, 27, 34, 41, 1]]
pos = 6


def convert_moves(pos, raw_moves):
    
    peacefull_moves = []
    normal_moves = []
    attack_moves = []
    stay_in_bounds = True
    
    while stay_in_bounds:
        stay_in_bounds = False
        for i in raw_moves:
            for a in i:                
                if  a < 1 or  a > 64:                   
                    if i.index(a) != len(i)-1:
                        i.pop(i.index(a))                        
                        stay_in_bounds = True

    print(raw_moves)
    for i in raw_moves:           
        if i[len(i)-1] == 0:
            i.pop(len(i)-1)
            for a in i:                   
                if a == pos:
                    peacefull_moves.append(i[(i.index(a)+1):])
                    peacefull_moves.append(list(reversed(i[:(i.index(a))])))
                    
                if type(i) == list:
                    if not pos in i:
                        peacefull_moves.append(i)
                        break

                    
                    
        if i[len(i)-1] == 1:
            i.pop(len(i)-1)
            for a in i:
                if a == pos:
                    normal_moves.append(i[(i.index(a)+1):])
                    normal_moves.append(list(reversed(i[:(i.index(a))])))
                
                if type(i) == list:
                    if not pos in i: 
                        normal_moves.append(i)
                        break
                    
        if i[len(i)-1] == 2:
            i.pop(len(i)-1)
            for a in i:
                if a == pos:
                    attack_moves.append(i[(i.index(a)+1):])
                    attack_moves.append(list(reversed(i[:(i.index(a))])))
                    
                if type(i) == list:
                    if not pos in i:
                        attack_moves.append(i)
                        break
                
#    peacefull_moves.sort()
#    normal_moves#.sort()
#    attack_moves#.sort()
#                     
    return([peacefull_moves, normal_moves, attack_moves])


if __name__ == '__main__':
    print(convert_moves(pos, raw_moves))