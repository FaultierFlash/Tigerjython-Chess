
def check_move_collisions(all_pieces, converted_moves):
    moves = []
    attack_moves = []
    
    for i in converted_moves[0]:
        for j in i:
            for k in all_pieces:
                if k.pos == j:
                    stop = True
        if stop:
            break
        else:
            moves.append(j)
            
    for i in converted_moves[1]:
        for j in i:
            for k in all_pieces:
                if k.pos == j:
                    stop = True
        if stop:
            attack_moves.append(j)
            break
        else:
            moves.append(j)
            
        
    for i in converted_moves[2]:
        for j in i:
            for k in all_pieces:
                if k.pos == j:
                    stop = True
        if stop:
            attack_moves.append(j)
            break
            
    
    return([moves, attack_moves])
            


if __name__ == '__main__':
    converted_moves = [[[46, 55, 64], [28, 19, 10, 1]], [[46, 55, 64], [28, 19, 10, 1]], [[46, 55, 64], [28, 19, 10, 1]]]
    All_pos = [1,2,3,4,8,9,5,64]

    print(converted_moves)
    print(check_move_collisions(all_pieces, converted_moves))