import random
import pyglet 
from pyglet import *
from pyglet.image.codecs.png import PNGImageDecoder
from dicework import *
from MenuTrial import *

#import key,mouse
win  = pyglet.window.Window( 800 ,900)
circle_x  = win.width // 10
circle_y  = win.height // 4.5
size_circle = 20
d  =  0
pos = 1
direction  = 1 
x =  0
up = 0
dice = 0

@win.event 
def on_dice() :
    global x 
    global dice
    global up 
    global pos
    global direction
    dice =  random.randint(1,6)
    print(dice,"was rolled")
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
                   
        
        
@win.event
def on_draw() :
          win.clear()
          global d 
          global up
          global dice
          d +=1 
          batch = pyglet.graphics.Batch()
                  
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
def on_game() :
    global circle_x
    global circle_y
    global pos 
    global up 
    global direction
    print("up:",up)
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

@win.event
def on_up() :
    global circle_y 
    global up
    if up<9 :
        circle_y += 65
        up += 1
    if up==9 :
        pass
@win.event
def on_down() :
    global circle_y 
    circle_y -= 65
@win.event
def on_right() :
    global circle_x
    global up 
    if up<9 :
        circle_x += 65
@win.event
def on_left() :
    global circle_x    
    circle_x -= 65
    
@win.event
def on_entry() :
    pass
@win.event
def on_key_press(symbol, modifier):
    global enter 
    
    if symbol == pyglet.window.key.UP :
        print("Key UP is pressed")
        on_up()
    if symbol == pyglet.window.key.DOWN :
        print("Key DOWN is pressed")
        on_down()
    if symbol == pyglet.window.key.LEFT :
        print("Key LEFT is pressed")
        on_left()
    if symbol == pyglet.window.key.RIGHT :
        print("Key RIGHT is pressed")
        on_right()

    if symbol==pyglet.window.key.ENTER :
        on_draw()
        # enter  += 1 
         
    if symbol == pyglet.window.key.SPACE :
        on_dice()
    if symbol == pyglet.window.key.ESCAPE:
        print(" exited ")
        win.close()
    else:
        pass


