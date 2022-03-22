from gturtle import *
tf = TurtleFrame()
t = Turtle(tf)
u = Turtle(tf)
delay(500)
tf.enableRepaint(False)
del t
tf.enableRepaint(True)
reload(Playground)
#t.fd(20)
