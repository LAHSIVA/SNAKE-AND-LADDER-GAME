import pyglet 
from pyglet import *
from pyglet.image.codecs.png import PNGImageDecoder

d1 = pyglet.image.load('dice1.png', decoder=PNGImageDecoder())

d2 = pyglet.image.load('dice2.png', decoder=PNGImageDecoder())

d3 = pyglet.image.load('dice3.png', decoder=PNGImageDecoder())

d4= pyglet.image.load('dice4.png', decoder=PNGImageDecoder())

d5 = pyglet.image.load('dice5.png', decoder=PNGImageDecoder())

d6= pyglet.image.load('dice6.png', decoder=PNGImageDecoder())

# dice = random.randint(1,6)
# win  = pyglet.window.Window(800,800)
def DICE( dice ) :
    if dice ==1 :
              sprite = pyglet.sprite.Sprite(d1,725,205)
              sprite.draw()
    if dice ==2 :
              sprite = pyglet.sprite.Sprite(d2,725,205)
              sprite.draw()
    if dice ==3 :
              sprite = pyglet.sprite.Sprite(d3, 725,205)
              sprite.draw()
    if dice ==4 :
              sprite = pyglet.sprite.Sprite(d4,725,205)
              sprite.draw()
    if dice ==5 :
              sprite = pyglet.sprite.Sprite(d5,725,205)
              sprite.draw()
    if dice ==6 :
              sprite = pyglet.sprite.Sprite(d6,725,205)
              sprite.draw()
'''
@win.event
def dice_draw() :
    sprite2.draw()
'''