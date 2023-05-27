import pyglet 
from pyglet import shapes 
from pyglet.image.codecs.png import PNGImageDecoder
def Rectangle(x,y,w) :
        batch = pyglet.graphics.Batch()
        co_x = x-30
        co_y = y
        width = w-20 
        height = 60
        color = (0,0,0)
        rec1 = shapes.Rectangle(co_x, co_y, width, height, color = color, batch = batch)
        # changing opacity of the rect1
        # opacity is visibility (0 = invisible, 255 means visible)
        rec1.opacity = 80
        batch.draw()   