import bishop_moves as b
import rook_moves as r

def queen_moves(pos):   
    l = r.rook_moves(pos)
    l.extend(b.bishop_moves(pos))
    return l

if __name__ == '__main__':
    print(queen_moves(20))
