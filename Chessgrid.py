from gturtle import *
import time as t
setPlaygroundSize(700, 700)
Xv = 8         #Die Breite des Schachbretts in Feldern
Yv = 8         #Die Höhe des Schachbretts in Feldern
makeTurtle()
ht()
setPenColor("grey") 

def schachfeld(Xv, Yv):
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

def make_color(first, second):
    draw_grid = True
    size = getPlaygroundWidth()*0.8/Xv
    P = (-0.8*getPlaygroundWidth()/2, -0.8*getPlaygroundHeight()/2)
    field_1 = 1
    x = size/2
    for i in range(8):
        for j in range(8):
            #delay(100)     
            if j%2 == 1:
                if i%2 == 1:
                    setFillColor(second)
                    setPos((P[0]+x+j*size),(P[1]+x+i*size))
                    fill()
                else:
                    setFillColor(first)
                    setPos((P[0]+x+j*size),(P[1]+x+i*size))
                    fill()
            else:
                if i%2 == 1:
                    setFillColor(first)
                    setPos((P[0]+x+j*size),(P[1]+x+i*size))
                    fill()
                else:
                    setFillColor(second)
                    setPos((P[0]+x+j*size),(P[1]+x+i*size))
                    fill()
        j += 1
    i += 1
   
def draw_moves(moves, field):
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
    
first = "#a35233"  #Die erste Feldfarbe
second = "#d6834f" #Die zweite Feldfarbe
moves = "#ffba08"  #Move-Feldfarbe

if __name__ == '__main__':
    T = t.time()
    schachfeld(Xv, Yv)
    #showTurtle()
    print(t.time()-T)
    make_color(first, second)
    print(t.time()-T)
    l = [-1]
    #l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64]
    for i in range(len(l)):
        field = l[i]
        draw_moves(moves, field)

    