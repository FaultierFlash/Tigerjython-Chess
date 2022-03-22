import Chessgrid
from gturtle import *

Xv = 8         #Die Breite des Schachbretts in Feldern
Yv = 8         #Die Höhe des Schachbretts in Feldern
first = "#a35233"  #Die erste Feldfarbe
second = "#d6834f" #Die zweite Feldfarbe

Chessgrid.schachfeld(Xv, Yv)
Chessgrid.make_color(first, second)
P = (-0.8*getPlaygroundWidth()/2, 0.8*getPlaygroundHeight()/2)
size = getPlaygroundWidth()*0.8/Xv

def coords(x, y):
    x, y = int((x-P[0])/size), int((y-P[1])/size)
    field = (y*-8 + x)+1
    print(field)

def get_started():
    global end    
    end = False
    
    while end==False:
        onMouseClicked(coords)
        
        if getKeyCode() == 10:
              end = True
              
get_started()