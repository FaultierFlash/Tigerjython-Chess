from gturtle import *
import time as t
Xv, Yv = 8, 8
width = 700
height = 700
setPlaygroundSize(width, height)
sprites = {
'p': "sprites/chessblack_5.png",
'r': "sprites/chessblack_2.png",
'n': "sprites/chessblack_3.png",
'q': "sprites/chessblack_1.png",
'b': "sprites/chessblack_4.png",
'k': "sprites/chessblack_0.png",
'P': "sprites/chesswhite_5.png",
'R': "sprites/chesswhite_2.png",
'N': "sprites/chesswhite_3.png",
'Q': "sprites/chesswhite_1.png",
'B': "sprites/chesswhite_4.png",
'K': "sprites/chesswhite_0.png"}



    
class board:
    def __init__(self, FEN, Xv, Yv, first, second):
        self.first = first
        self.second = second
        self.tf = TurtleFrame()
        self.turn = 0
        self.all_pieces = []
        self.Turtle = Turtle(self.tf)
        self.Turtle.ht()
        self.moves_Turtle = Turtle(self.tf)
        self.moves_Turtle.ht()
        self.FEN = FEN
        self.draw_board(Xv, Yv)
        self.all_pieces = self.summon_pieces(sprites, self.FEN)
        print(self.all_pieces)
        self.fen_in_pos(self.FEN)
        self.all_pieces = []
        self.player = player(True)
        
    def draw_board(self, Xv, Yv):
        Xs = width*0.8/Xv
        Ys = height*0.8/Yv
        self.Turtle.setPos(-0.8*width/2, -0.8*height/2)
        self.Turtle.setPenColor("grey")  
        for i in range(0, Xv):     
            for j in range(0, Yv):
                for k in range(0, 4):
                    self.Turtle.fd(Xs)
                    self.Turtle.rt(90)
                                   
                self.Turtle.fd(Xs)   
            self.Turtle.setPos(self.Turtle.getX()+Xs, self.Turtle.getY()-Xs*Yv)
        self.reset_board_color()
    
            
                
#    def reset_board_color(self):
#        size = width*0.8/Xv
#        P = (-0.8*width/2, -0.8*height/2)
#        self.Turtle.st()
#        print('reset color')
#        for i in range(8):
#            for j in range(8):
#                #delay(10)     
#                if j%2 == 1:
#                    if i%2 == 1:
#                        self.Turtle.setFillColor(second)
#                        self.Turtle.fill((P[0]+2+j*size),(P[1]+2+i*size))
#                    else:
#                        self.Turtle.setFillColor(first)
#                        self.Turtle.fill((P[0]+2+j*size),(P[1]+2+i*size))
#                else:
#                    if i%2 == 1:
#                        self.Turtle.setFillColor(first)
#                        self.Turtle.fill((P[0]+2+j*size),(P[1]+2+i*size))
#                    else:
#                        self.Turtle.setFillColor(second)
#                        self.Turtle.fill((P[0]+2+j*size),(P[1]+2+i*size))
#            j += 1
#        i += 1 
#        return(True)
    
                
    def reset_board_color(self):
        print('reset')
        second_color = [1,3,5,7,10,12,14,16,17,19,21,23,26,28,30,32,33,35,37,39,42,44,46,48,49,51,53,55,58,60,62,64]
        first_color = [2,4,6,8,9,11,13,15,18,20,22,24,25,27,29,31,34,36,38,40,41,43,45,47,50,52,54,56,57,59,61,63]
        
        
        for i in first_color:
            self.Turtle.setFillColor(first)
            pos = self.calculate_field(i)
            self.Turtle.setPos(pos[0], pos[1])
            self.Turtle.fill()
        
        
        for i in second_color:
            self.Turtle.setFillColor(second)
            pos = self.calculate_field(i)
            self.Turtle.setPos(pos[0], pos[1])
            self.Turtle.fill()
            
        return(True)
    
    def calculate_field(self, field):
        size = width*0.8/Xv
        P = (-0.8*width/2+size*0.5, 0.8*height/2-size*0.5)
        field_x = field%8
        
        if field_x == 0:
            field_x = 8
            
        if field%8 == 0:
            field_y = (field//9)+1
            
        else:
            field_y = (field//8)+1
            
        return((P[0]+((field_x-1)*size)),(P[1]-((field_y-1)*size)))   
    
    def fen_in_pos(self, FEN):
        l = []
        y_pos = 0
        x_pos = 0
        finished = False
                
        for i in FEN:
            if i == "/":
                y_pos += 1
                x_pos = 0
            elif i.isnumeric():
                x_pos += int(i)
                
            elif i == " ":
                finished = True
            
            elif not finished:
                x_pos += 1
                piece = i
                l.append(piece + str(y_pos*8+x_pos))
                
        return(l)    

    def summon_pieces(self, sprites, FEN):
        dialoge = askYesNo("Möchtest du mit einem FEN spielen? ", False)
        
        if dialoge:
            FEN = inputString("FEN: ")
            
        else:
            pass
        
        l = self.fen_in_pos(FEN)
        
        for i in l:
            piece = i[0]
            pos = int(i[1:])
            #T = Turtle(self.tf, sprites[str(piece)], turtleHit = onTurtleHit).setPos(pos_x, pos_y)
            self.all_pieces.append(chess_piece(self, piece, pos))
            
        return(self.all_pieces)
    

class chess_piece:
    def __init__(self, board, piece, pos):
        self.color = piece.isupper()
        self.board = board
        self.all_pieces = board.all_pieces
        #print(self.board.all_pieces)
        self.overturtle = board.Turtle
        self.pos = pos
        self.coords = board.calculate_field(self.pos)
        self.pos_x = self.coords[0]
        self.pos_y = self.coords[1]
        self.piece = piece
        self.moved = False
        self.Turtle = Turtle(board.tf, sprites[str(self.piece)], turtleHit = self.register_klick)
        self.Turtle.setPos(self.pos_x, self.pos_y)
        self.has_moved = True
        self.overturtle.addMouseHitListener(self.move_piece)
        
        
        
    def register_klick(self, turtle, x, y):

        
        if self.board.player.turn_color == self.color:
            #print(self.all_pieces)
            T = t.time()
            self.board.tf.enableRepaint(False)
            self.board.reset_board_color()
            self.board.tf.enableRepaint(True)
            print(t.time()-T)
            
            self.raw_moves = self.get_moves(self.piece, self.pos, self.moved, self.color)
            #print(self.raw_moves)
            self.converted_moves = self.convert_moves(self.pos, self.raw_moves)
            self.moves = self.moves = self.check_move_collisions(self.all_pieces, self.converted_moves, self.color)
            self.has_moved = False
            print(t.time()-T)
            for j in self.moves[0]:
                self.show_moves('green', j)
                
            for j in self.moves[1]:
                self.show_moves('red', j)
            
            print(t.time()-T)
            
            return(True)
    
    def move_piece(self, x, y):
        if not self.has_moved:
            killed = False
            T = t.time()
            try:
                self.Turtle == None
        
            except AttributeError:
                return()
            
            
            if not self.has_moved:
                field = self.get_field(x, y)
                if field in self.moves[1]:
                    print('move time 1: ' + str(t.time()-T) + ' attack')
                    for i in self.all_pieces:
                        if i.pos == field:
                            i.kill()
                            killed = True
                            break
                    if killed:
                        future_coords = self.get_coords(field)
                        self.Turtle.setPos(future_coords[0], future_coords[1])
                        print('move time 2: ' + str(t.time()-T))
                        #self.board.tf.enableRepaint(False)
                        if not self.board.reset_board_color():
                            return
                        #self.board.tf.enableRepaint(True)
                        print('move time 3: ' + str(t.time()-T))
                        self.pos = field
                        self.has_moved = True
            
                    
                elif field in self.moves[0]:
                    self.pos = field
                    print('move time 1: ' + str(t.time()-T) + ' move')
                    self.board.tf.enableRepaint(False)
                    if not self.board.reset_board_color():
                        return
                    self.board.tf.enableRepaint(True)
                    print('move time 2: ' + str(t.time()-T))
                    future_coords = self.get_coords(field)
                    self.Turtle.setPos(future_coords[0], future_coords[1])
                    self.has_moved = True
                    print('move time 3: ' + str(t.time()-T))
                    
                    #print(self.board.player.turn_color)
            if self.has_moved:
                self.board.player.turn_color = not self.color
                print(self.board.player.turn_color)
            print('move time 4: ' + str(t.time()-T) + ' killed: ' + str(killed))
            print('done')
            return(self.has_moved)
            
            
    
    def get_coords(self, field):
        size = width*0.8/Xv
        start_position = ((-0.8*width/2)+size*0.5, (0.8*height/2)+size*0.5)
        field_x = field%8
        if field_x == 0:
            field_x = 8
        if field%8 == 0:
            field_y = (field//9)+1
        else:
            field_y = (field//8)+1
        return((start_position[0]+(field_x*size)-size, start_position[1]-(field_y*size)))

    def get_field(self, x, y):
        Xv = 8
        P = (-0.8*width/2, 0.8*height/2)
        size = width*0.8/Xv
        x, y = int((x-P[0])/size), int((y-P[1])/size)
        field = (y*-8 + x)+1
        return(field)
    
    def get_moves(self, piece, pos, moved, color):
        import bishop_moves as b
        import rook_moves as r
        import knight_moves as n
        import queen_moves as q
        import king_moves as k
        import pawn_moves as p

        if piece == 'p' or piece == 'P':
            if self.pos < 17 and self.pos > 8 or self.pos < 57 and self.pos > 48:
                moved = False
            else:
                moved = True
            m = p.pawn_moves(pos, moved, color)
            
        elif piece == 'r' or piece == 'R':
            m = r.rook_moves(pos)
            
        elif piece == 'b' or piece == 'B':
            m = b.bishop_moves(pos)
    
        elif piece == 'n' or piece == 'N':
            m = n.knight_moves(pos)
    
        elif piece == 'q' or piece == 'Q':
            m = q.queen_moves(pos)
            
        elif piece == 'k' or piece == 'K':
            m = k.king_moves(pos)
            
        return(m)
    
    def convert_moves(self, pos, raw_moves):
        
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

    
    def check_move_collisions(self, all_pieces, converted_moves, color):
        moves = []
        attack_moves = []
        stop = False
        j = None
        
        for i in converted_moves[0]:
            for j in i:
                for k in all_pieces:
                    if k.pos == j:
                        stop = True
                if stop or j == None:
                    break
                else:
                    moves.append(j)
                    
            
        stop = False
        
        for i in converted_moves[1]:
            stop = False
            for j in i:
                #print(self.board.all_pieces)
                for k in all_pieces:
                    
                    if k.pos == j:
                        if k.color != color:
                            attack_moves.append(j)
                        stop = True
                        break
                        
                if stop or j == None:
                    break
                else:
                    moves.append(j)
                
            
        stop = False
        
        for i in converted_moves[2]:
            for j in i:
                for k in all_pieces:
                    if k.pos == j:
                        if k.color != color:
                            attack_moves.append(j)
                        stop = True
            if stop or j == None:
                break
                
        
        return([moves, attack_moves])
    
    def kill(self):
        try:
            self.Turtle.setPos(width, height)
            delay(100)
            self.Turtle.ht()
        except AttributeError:
            return
        del self.Turtle
        for i in range(0, len(self.all_pieces)):
            if self.all_pieces[i] == self:
                del self.all_pieces[i]
                print('deleted')
                break
        #del self
    
    def __del__(self):
        print('success')
            
    def show_moves(self, moves, field):
        size = width*0.8/Xv
        start_position = ((-0.8*width/2)+size*0.5, (-0.8*height/2)+size*0.5)
        #self.board.Turtle.showTurtle()
        self.board.moves_Turtle.setPos((-0.8*width/2)+size*0.5, (-0.8*height/2)+size*0.5)
        field_x = field%8
        if field_x == 0:
            field_x = 8
        if field%8 == 0:
            field_y = (field//9)+1
        else:
            field_y = (field//8)+1
        field_to_fill = (start_position[0]+(field_x*size)-size, start_position[1]+size*8-(field_y*size))
        self.board.moves_Turtle.setFillColor(moves)
        #print(field_to_fill)
        self.board.moves_Turtle.setPos(field_to_fill[0], field_to_fill[1])
        self.board.moves_Turtle.fill()
    
    def check_king():
        pass
        
    def promote():
        pass
      
        
class player:
    def __init__(self, turn_color):
        self.turn_color = turn_color
    def get_points():
        pass

FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"            
first = "#a35233"  #Die erste Feldfarbe
second = "#d6834f" #Die zweite Feldfarbe
                                                                      
board(FEN, Xv, Yv, first, second)


     
                    
     
                            
                                        
