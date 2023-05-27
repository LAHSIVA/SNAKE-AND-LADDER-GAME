import pyglet
from pyglet import *
from rectangle import *
from pyglet.image.codecs.png import PNGImageDecoder
# win  = pyglet.window.Window( 800 ,900)
def Menu():
        pic  =  pyglet.image.load('backgroundmenu.png', decoder=PNGImageDecoder()) 
        sprite = pyglet.sprite.Sprite(pic)
        top = 'Snake and Ladder Game'
        label = pyglet.text.Label(top ,
                                    font_name='Algerian',
                                    font_size= 30 ,                
                                    x  = 800//2,
                                    y =  900//1.1,
                                    anchor_x='center',
                                    anchor_y='top')
        label.color = ( 255,250,255,500)
        sprite.draw()
        label.draw()
        play = "PLAY"
        multi = "PLAY 1-V-1 "
        label2 = pyglet.text.Label(play,
                                   font_name="Algerian",
                                   font_size = 40 , 
                                     x  = 380 ,
                                     y = 550  ,
                                     anchor_x= 'center'
        )
        
        label3 = pyglet.text.Label(multi,
                                   font_name="Algerian",
                                   font_size = 35 , 
                                     x  = 380 ,
                                     y = 435  ,
                                     anchor_x= 'center'
        )
        label2.draw()
        label3.draw()
        #surface()# MENU()
#pyglet.app.run()
