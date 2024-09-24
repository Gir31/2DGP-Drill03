from pico2d import *
import math
    
open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x, y):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.05)  

def run_top():
    print('TOP')
    for x in range(0, 800,10):
        draw_boy(x, 550)
    pass

def run_right():
    print('RIGHT')
    for y in range(550, 0, -10):
        draw_boy(800, y)
    pass

def run_bottom():
    print('BOTTOM')
    for x in range(800, 0, -10):
        draw_boy(x, 50)
    pass

def run_left():
    print('LEFT')
    for y in range(0, 550, 10):
        draw_boy(0, y)
    pass

def triangle_left():
    print('TRIANGLE LEFT')
    for h in range(0, 400, 4):
        draw_boy(h, h)
    pass

def triangle_right():
    print('TRIANGLE RIGHT')
    cx, cy = 400, 400
    for h in range(0, 400, 4):
        x, y = cx + h, cy - h
        draw_boy(x, y)
    pass

def run_rectangle():
    print('RECTANGLE')
    run_top()
    run_right()
    run_bottom()
    run_left()
    pass

def run_circle():
    print('CIRCLE')

    r, cx, cy = 300,800//2, 600//2

    for d in range(0,360):
        x = r*math.cos(math.radians(d)) + cx
        y = r*math.sin(math.radians(d)) + cy
        draw_boy(x, y)  
        
    
    pass

def run_triangle():
    print('TRIANGLE')
    #run_bottom()
    triangle_left()
    triangle_right()
    pass



while (True):
    #run_circle()
    #run_rectangle()
    run_triangle()
    break

close_canvas()
