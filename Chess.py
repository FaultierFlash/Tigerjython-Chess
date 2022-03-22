from gturtle import *
import bishop_moves as b
import rook_moves as r
import knight_moves as k
import queen_moves as q
import king_moves as ki
import pawn_moves as p
import Chessgrid as Cg

sprites = {
'b_Pawn': "sprites/chessblack_5.png",
'b_Rook': "sprites/chessblack_2.png",
'b_Knight': "sprites/chessblack_3.png",
'b_Bishop': "sprites/chessblack_1.png",
'b_Queen': "sprites/chessblack_4.png",
'b_King': "sprites/chessblack_0.png",
'w_Pawn': "sprites/chesswhite_5.png",
'w_Rook': "sprites/chesswhite_2.png",
'w_Knight': "sprites/chesswhite_3.png",
'w_Bishop': "sprites/chesswhite_1.png",
'w_Queen': "sprites/chesswhite_4.png",
'w_King': "sprites/chesswhite_0.png"}

class board:
    def __init__(self):
        self.tf = TurtleFrame()
        self.turn = 0
        self.all_pieces = []
        
    def draw_board(Xv, Yv):
        Xs = getPlaygroundWidth()*0.8/Xv
        Ys = getPlaygroundHeight()*0.8/Yv
        setPos(-0.8*getPlaygroundWidth()/2, -0.8*getPlaygroundHeight()/2)   
        repeat Xv:     
            repeat Yv:
                repeat 4:
                    fd(Xs)
                    rt(90)
                                   
                fd(Xs)   
            setPos(getX()+Xs, getY()-Xs*Yv)
            
    def reset_board_color():
        draw_grid = True
        size = getPlaygroundWidth()*0.8/Xv
        P = (-0.8*getPlaygroundWidth()/2, -0.8*getPlaygroundHeight()/2)
        field_1 = 1
        for i in range(8):
            for j in range(8):     
                if j%2 == 1:
                    if i%2 == 1:
                        setFillColor(second)
                        fill((P[0]+size*0.5+j*size),(P[1]+size*0.5+i*size))
                    else:
                        setFillColor(first)
                        fill((P[0]+size*0.5+j*size),(P[1]+size*0.5+i*size))
                else:
                    if i%2 == 1:
                        setFillColor(first)
                        fill((P[0]+size*0.5+j*size),(P[1]+size*0.5+i*size))
                    else:
                        setFillColor(second)
                        fill((P[0]+size*0.5+j*size),(P[1]+size*0.5+i*size))
            j += 1
        i += 1
    

class chess_piece:
    def __init__(self, player, board, piece, pos):
        self.color = player.color
        self.pos = pos
        self.piece = piece
        self.moved = False
        self.Turtle = Turtle(board.tf, turtleHit = self.register_klick())
        
    def register_klick(self):
        if player.my_Turn == True:
            get_moves(self.piece, self.pos, self.moved, self.color)
            
    
    def get_moves(self, piece, pos, moved, color):
        if piece == 'pawn':
            m = p.pawn_moves(pos, moved, color)
            
        elif piece == 'rook':
            m = r.rook_moves(pos)
            
        elif piece == 'rook':
            m = p.bishop_moves(pos)
    
        elif piece == 'rook':
            m = k.knight_moves(pos)
    
        elif piece == 'rook':
            m = q.queen_moves(pos)
            
        elif piece == 'rook':
            m = ki.king_moves(pos)
            
        return(m)
    
    def convert_moves(pos, raw_moves):
        peacefull_moves = []
        normal_moves = []
        attack_moves = []
        stay_in_bounds = True
        try:
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
                            
                            
                            
                if i[len(i)-1] == 1:
                    i.pop(len(i)-1)
                    for a in i:
                        if a == pos:
                            normal_moves.append(i[(i.index(a)+1):])
                            normal_moves.append(list(reversed(i[:(i.index(a))])))
                            
                            
                if i[len(i)-1] == 2:
                    i.pop(len(i)-1)
                    for a in i:
                        if a == pos:
                            attack_moves.append(i[(i.index(a)+1):])
                            attack_moves.append(list(reversed(i[:(i.index(a))])))
                            
        except IndexError:
            pass
                        
        return([peacefull_moves, normal_moves, attack_moves])

    
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
            
                
            
         
    def move():
        
        if self.piece == pawn:
            
    
    def kill():
        
    def show_moves(moves, field):
        size = getPlaygroundWidth()*0.8/Xv
        start_position = ((-0.8*getPlaygroundWidth()/2)+size*0.5, (-0.8*getPlaygroundHeight()/2)+size*0.5)
        showTurtle()
        setPos(start_position)
        field_x = field%8
        if field_x == 0:
            field_x = 8
        if field%8 == 0:
            field_y = (field//9)+1
        else:
            field_y = (field//8)+1
        field_to_fill = (start_position[0]+(field_x*size)-size, start_position[1]+(field_y*size)-size)
        setFillColor(moves)
        fill(field_to_fill)
    
    def check_king():
        
    def promote():
        
        
class player:
    def __init__(self, color, ):
        self.color = color
        
    def get_points():
             

                
while True:
    
            
                
     x = chess_piece(white, pawn, 15)
     
                    
     
                            
                                        
