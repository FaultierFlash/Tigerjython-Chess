from gturtle import *
Xv = 8
P = (-0.8*getPlaygroundWidth()/2, 0.8*getPlaygroundHeight()/2)
size = getPlaygroundWidth()*0.8/Xv
tf = TurtleFrame()

#def hi(x, y):
#    print('hi')
#    print(str(x) + str(y))
class test:
    def __init__(self):
        self.t = Turtle(tf)
        #self.test()
        self.test_2 = test_2(self)
    
#test = test()


class test_2:
    def __init__(self, arg):
        self.t1 = arg
        self.test()
    def coords(self, x, y):
        x, y = int((x-P[0])/size), int((y-P[1])/size)
        field = (y*-8 + x)+1
        print(field)
        
        
    def test(self):
        self.t1.t.addMouseHitListener(self.coords)
    def test_test(self):
        self.test()
        print('hi')

test()
    