import pygame as py

def createCircle():
    SCREEN.fill((0, 0, 255))

def gravity(circle_y, g):
    if(circle_y < 350):
        circle_y = circle_y + g
    return circle_y

def jump(circle_y, jump): 
    return circle_y - jump


size = (500, 400)
SCREEN = py.display.set_mode(size)

circle_y = 50
GRAVITYDISTANCE = 0.04
JUMPDISTANCE = 40

while True:
    for ev in py.event.get():
        if ev.type == py.QUIT:
            py.display.quit()
        if ev.type == py.KEYDOWN:
            circle_y = jump(circle_y, JUMPDISTANCE)
    
    createCircle()
    circle_y = gravity(circle_y, GRAVITYDISTANCE)

    py.draw.ellipse(SCREEN, (255, 255, 0), (50, circle_y, 50, 50))
    py.display.update()



