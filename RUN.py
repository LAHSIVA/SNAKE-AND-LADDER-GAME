import random
import math  
import pyglet 
from pyglet import *
from pyglet.image.codecs.png import PNGImageDecoder
from dicework import *
from MenuTrial import *
from rectangle import *
#import key,mouse
win  = pyglet.window.Window( 800 ,900)
circle_x  = win.width // 10
circle_y  = win.height // 4.5
c2_x  = win.width // 10
c2_y  = win.height // 4.5

size_circle = 20
d  =  0

 
pos2 = 1
direction2  = 1 
x2 =  0
up2 = 0
 
pos = 1
direction  = 1 
x =  0
up = 0
dice = 0
enter = 0


y  = 0
w = 0
xr = 0
'''
d1 = pyglet.image.load('dice1.png', decoder=PNGImageDecoder())
d2 = pyglet.image.load('dice2.png', decoder=PNGImageDecoder())
d3 = pyglet.image.load('dice3.png', decoder=PNGImageDecoder())
d4 = pyglet.image.load('dice4.png', decoder=PNGImageDecoder())
d5 = pyglet.image.load('dice5.png', decoder=PNGImageDecoder())
d6 = pyglet.image.load('dice6.png', decoder=PNGImageDecoder())

if dice ==1 :
                  sprite2 = pyglet.sprite.Sprite(d1, 100, 100)
if dice ==2 :
                  sprite2 = pyglet.sprite.Sprite(d2, 100, 100)
if dice ==3 :
                  sprite2 = pyglet.sprite.Sprite(d3, 100, 100)
if dice ==4 :
                  sprite2 = pyglet.sprite.Sprite(d4, 100, 100)
if dice ==5 :
                  sprite2 = pyglet.sprite.Sprite(d5, 100, 100)
if dice ==6 :
                  sprite2 = pyglet.sprite.Sprite(d6, 100, 100)
'''

@win.event 
def on_dice() :
    global x 
    global x2 
    global d 
    global dice
    global up
    global up2
    global pos
    global pos2
    global direction
    global direction2 
    dice =  random.randint(1,6)
    print(dice,"was rolled")
    if d%2==1 :
        pos += dice
        if up <= 9 :
            if pos <10 and pos !=dice and direction ==1  :
                for i in range(dice) :
                    on_right()
                print("first if")
            elif pos==10 and direction==1 :
                for i in range(dice):
                    on_right()
                pos =0 
                print("2 if")
            elif pos==dice and direction ==1 :
                on_up()
                for i in range(dice-1) :
                    on_left()
                pos = dice
                direction = -1
                print("3 if")
            elif pos>10 and direction ==1  :
                pos -= 10
                temp = dice - pos
                for i in range(temp) :
                    on_right()
                on_up()
                direction = -1
                for i in range(pos-1) :
                    on_left()
                print("4 if")
            
            
            elif pos <10 and pos!=dice and direction ==-1 :
                    for i in range(dice):
                        on_left()
                    print("5 if")
            elif pos==10 and direction ==-1 :
                for i in range(dice) :
                    on_left()
                pos = 0
                print("6 if")
            elif pos==dice and direction==-1 :
                on_up()
                for i in range(dice-1):
                    on_right()
                pos = dice
                direction  = 1
                print("7 if")
        
            elif pos >10 and direction ==-1 :
                pos -= 10
                temp = dice - pos
                for i in range(temp) :
                    on_left()
                on_up()
                direction = 1
                for i in range(pos-1) :
                    on_right()
                print("8 if")
                      
            
            
            print(pos,direction)
            
        else :
            print(" Insufficient board moves ")
    if d%2==0 :
        pos2 += dice
        if up2 <= 9 :
            if pos2 <10 and pos2 !=dice and direction2 ==1  :
                for i in range(dice) :
                    on_right()
                print("first if")
            elif pos2==10 and direction2==1 :
                for i in range(dice):
                    on_right()
                pos2 =0 
                print("2 if")
            elif pos2==dice and direction2 ==1 :
                on_up()
                for i in range(dice-1) :
                    on_left()
                pos2 = dice
                direction2 = -1
                print("3 if")
            elif pos2>10 and direction2 ==1  :
                pos2 -= 10
                temp = dice - pos2
                for i in range(temp) :
                    on_right()
                on_up()
                direction2 = -1
                for i in range(pos2-1) :
                    on_left()
                print("4 if")
            
            
            elif pos2 <10 and pos2!=dice and direction2 ==-1 :
                    for i in range(dice):
                        on_left()
                    print("5 if")
            elif pos2==10 and direction2 ==-1 :
                for i in range(dice) :
                    on_left()
                pos2 = 0
                print("6 if")
            elif pos2==dice and direction2==-1 :
                on_up()
                for i in range(dice-1):
                    on_right()
                pos2 = dice
                direction2  = 1
                print("7 if")
        
            elif pos2 >10 and direction2 ==-1 :
                pos2 -= 10
                temp = dice - pos2
                for i in range(temp) :
                    on_left()
                on_up()
                direction2 = 1
                for i in range(pos2-1) :
                    on_right()
                print("8 if")
                      
            
            
            print(pos2,direction2)
            
        else :
            print(" Insufficient board moves ")
@win.event        
def on_draw2() :
    global d 
    global up
    global dice
    d +=1 
    batch = pyglet.graphics.Batch()
    if d==1 :
        '''
        pic  =  pyglet.image.load('snakemenu1.png', decoder=PNGImageDecoder()) 
        sprite = pyglet.sprite.Sprite(pic)
        label = pyglet.text.Label('Snake and Ladder Game',
                                font_name='Algerian',
                                font_size= 25 ,
                        
                                x  = win.width//2,
                                y =  win.height//1.1,
                                anchor_x='center',
                                anchor_y='top')
        label.color = ( 0,0,0,4000)
        sprite.draw()
        label.draw()
        '''
        Menu()
        
    else  :
          
          bg = pyglet.image.load('bgs3.png', decoder=PNGImageDecoder())
          sprite = pyglet.sprite.Sprite(bg, 44, 167)
          sprite.draw()

        #dice  = random.randint(1,6)
          global circle_x 
          global circle_y 
        
          print(circle_x," :" , circle_y)
        # size of circle
        # color = green
          
          str1 = []
          str1.append(dice)
          str1.append(" was rolled ")
          str2  = str(str1[0])
          str2 = str2 + " was rolled "
          
          DICE(dice) 
          size_circle = 25
          batch2 = pyglet.graphics.Batch()
          circle = shapes.Circle(circle_x, circle_y, size_circle, color =(0,0,139), batch = batch2) 
    # changing opacity of the circle1
    # opacity is visibility (0 = invisible, 255 means visible)
          circle.opacity = 170    
          batch2.draw()
         
          #dice_draw()
          label2 = pyglet.text.Label(str2,
                                font_name='Helvetica',
                                font_size= 25 ,
                                x  = 590 ,
                                y =  120 ,
                                anchor_x='center',
                                anchor_y='bottom')
          if dice >=1  :
              label2.draw()
          on_game()
          circle = shapes.Circle(circle_x, circle_y, size_circle, color =(0,0,139), batch = batch2)
          batch2.draw()
    if circle_x==80 and circle_y==785.0 :
                label = pyglet.text.Label('victory ! game over ',
                                font_name='Algerian',
                                font_size= 25 ,
                                x  = win.width//2,
                                y =  win.height//1.7,
                                anchor_x='center',
                              anchor_y='top')
                win.clear()
                label.draw()
    #on_game()

@win.event
def on_draw() :
    win.clear()
    global d 
    global up
    global dice
    global enter 
    batch = pyglet.graphics.Batch()
    if enter==0  :
        global y
        global xr
        global w
        '''
        pic  =  pyglet.image.load('snakemenu1.png', decoder=PNGImageDecoder()) 
        sprite = pyglet.sprite.Sprite(pic)
        label = pyglet.text.Label('Snake and Ladder Game',
                                font_name='Algerian',
                                font_size= 25 ,
                        
                                x  = win.width//2,
                                y =  win.height//1.1,
                                anchor_x='center',
                                anchor_y='top')
        label.color = ( 0,0,0,4000)
        sprite.draw()
        label.draw()
        '''
        Menu()
        Rectangle(xr,y,w)
       
    if enter == 1  :
          d += 1 
          bg = pyglet.image.load('bgs3.png', decoder=PNGImageDecoder())
          sprite = pyglet.sprite.Sprite(bg, 44, 167)
          sprite.draw()

        #dice  = random.randint(1,6)
          global circle_x 
          global circle_y 
          global c2_x
          global c2_y
        
          print(circle_x," :" , circle_y)
        # size of circle
        # color = green
          str1 = []
          str1.append(dice)
          str1.append(" was rolled ")
          str2  = str(str1[0])
          str2 = str2 + " was rolled "
          
          DICE(dice) 
          size_circle = 25
          batch2 = pyglet.graphics.Batch()
          circle = shapes.Circle(circle_x, circle_y, size_circle, color =(0,128,0), batch = batch2) 
    # changing opacity of the circle1
    # opacity is visibility (0 = invisible, 255 means visible)
          circle.opacity = 170    
          # batch2.draw()
         
          batch3 = pyglet.graphics.Batch()
          circle2 = shapes.Circle(c2_x, c2_y, size_circle, color =(0,0,0), batch = batch2) 
    # changing opacity of the circle1
    # opacity is visibility (0 = invisible, 255 means visible)
          circle2.opacity = 170    
          # batch3.draw()
         
          #dice_draw()
          label2 = pyglet.text.Label(str2,
                                font_name='Helvetica',
                                font_size= 25 ,
                                x  = 590 ,
                                y =  120 ,
                                anchor_x='center',
                                anchor_y='bottom')
          if dice >=1  :
              label2.draw()
          if d%2==1 :
              batch2.draw()
              batch3.draw()
              on_game()

              circle = shapes.Circle(circle_x, circle_y, size_circle, color =(0,128,0), batch = batch2)
              batch2.draw()
              batch3.draw()
          if d%2==0 :

              batch3.draw()
              batch2.draw()
              on_game()
              circle = shapes.Circle(c2_x, c2_y, size_circle, color =(0,0,0), batch = batch3)
              batch2.draw()
              batch3.draw()
              
          # batch2.draw()
    if circle_x==80 and circle_y==785.0 :
                label = pyglet.text.Label(' GREEN - victory ! game over ',
                                font_name='Algerian',
                                font_size= 25 ,
                                x  = win.width//2,
                                y =  win.height//1.7,
                                anchor_x='center',
                                anchor_y='top')
                win.clear()
                label.draw()
    if c2_x==80 and c2_y==785.0 :
                label = pyglet.text.Label('BLACK - victory ! game over ',
                                font_name='Algerian',
                                font_size= 25 ,
                                x  = win.width//2,
                                y =  win.height//1.7,
                                anchor_x='center',
                                anchor_y='top')
                win.clear()
                label.draw()
    
    
    
    #on_game()
@win.event
def on_game() :

    global circle_x
    global circle_y
    global pos 
    global up 
    global direction
    global pos2 
    global up2 
    global direction2
    global d 
    global c2_x
    global c2_y
    print("up:",up)
    if d%2==1 :
        if circle_x==600 and circle_y==200 :
            circle_x = 535
            circle_y = 460
            pos = 8
            direction = 1
            up =4
        if circle_x==210 and circle_y==395 :
            circle_x = 145
            circle_y = 785
            pos = 9
            direction = -1
            up=9
        if circle_x==405 and circle_y==525 :
            circle_x = 470
            circle_y = 655
            pos = 4
            direction = -1
            up=7
        if circle_x==210 and circle_y==590 :
            circle_x = 275
            circle_y = 720
            pos = 4
            direction = 1
            up = 8
            
        if circle_x==210 and circle_y==525 :
            circle_x=405
            circle_y=200
            pos = 6
            direction = 1
            up = 0
        if circle_x==210 and circle_y==720 :
            circle_x=145
            circle_y=590
            pos = 2
            direction = 1
            up = 6
        if circle_x==340 and circle_y==785 :
            circle_x=600
            circle_y=590
            pos = 9
            direction = 1
            up = 6
        if circle_x==405 and circle_y==590 :
            circle_x=80
            circle_y=200
            pos = 1
            direction = 1
            up = 0 
    if d%2==0 :
        if c2_x==600 and c2_y==200 :
            c2_x = 535
            c2_y = 460
            pos2 = 8
            direction2 = 1
            up2 =4
        if c2_x==210 and c2_y==395 :
            c2_x = 145
            c2_y = 785
            pos2 = 9
            direction2 = -1
            up2 =9
        if c2_x==405 and c2_y==525 :
            c2_x = 470
            c2_y = 655
            pos2 = 4
            direction2 = -1
            up2=7
        if c2_x==210 and c2_y==590 :
            c2_x = 275
            c2_y = 720
            pos2 = 4
            direction2 = 1
            up2 = 8
            
        if c2_x==210 and c2_y==525 :
            c2_x=405
            c2_y=200
            pos2 = 6
            direction2 = 1
            up2 = 0
        if c2_x==210 and c2_y==720 :
            c2_x=145
            c2_y=590
            pos2 = 2
            direction2 = 1
            up2 = 6
        if c2_x==340 and c2_y==785 :
            c2_x=600
            c2_y=590
            pos2 = 9
            direction2 = 1
            up2 = 6
        if c2_x==405 and c2_y==590 :
            c2_x=80
            c2_y=200
            pos2 = 1
            direction2 = 1
            up2 = 0 
        
@win.event
def on_up() :
    global circle_y 
    global c2_y
    global up
    global up2 
    global enter
    global d  
    if enter ==1 and d%2==1  :
        if up<9 :
            circle_y += 65
            up += 1
        if up==9 :
                pass
    
    if enter ==1 and d%2==0  :
        if up2<9 :
            c2_y += 65
            up2 += 1
        if up2==9 :
            pass


@win.event
def on_down() :
    global enter 
    global d
    if enter == 1 and d%2==1  :
        global circle_y 
        circle_y -= 65
    if enter == 1 and d%2==0  :
        global c2_y 
        c2_y -= 65
@win.event
def on_right() :
    global circle_x
    global c2_x
    global d
    global up 
    global up2 
    if up<9 and d%2==1 :
        circle_x += 65
    if up2<9 and d%2==0 :
        c2_x += 65
@win.event
def on_left() :
    global circle_x    
    global c2_x
    global d
    if d%2==1 :
        circle_x -= 65
    if d%2==0 :
        c2_x -= 65
        
@win.event
def on_entry() :
    pass
@win.event
def on_key_press(symbol, modifier):
    global enter 
    global y 
    global xr
    global w 
    if symbol == pyglet.window.key.UP :
        print("Key UP is pressed")
        if enter ==1  :
            on_up()
        if enter==0 :
            y = 548
            xr = 325
            w = 200
    if symbol == pyglet.window.key.DOWN :
        print("Key DOWN is pressed")
        if enter ==1  :
            on_down()
        if enter==0 :
            y = 430
            xr = 275
            w = 295
    if symbol == pyglet.window.key.LEFT :
        print("Key LEFT is pressed")
        on_left()
    if symbol == pyglet.window.key.RIGHT :
        print("Key RIGHT is pressed")
        on_right()
    if symbol==pyglet.window.key.ENTER and w==295 :
        import Multiplayer
        win.close()
        enter = 1 
    elif symbol==pyglet.window.key.ENTER and w==200 :
        import SINGLE
        win.close()
        enter = 1
    if symbol == pyglet.window.key.SPACE :
        if enter ==1  :
            on_dice()
    if symbol == pyglet.window.key.ESCAPE:
        print(" exited ")
        win.close()
    else:
        pass

pyglet.app.run()



