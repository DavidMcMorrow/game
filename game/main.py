import pygame as py
import constants
import pipe

def createCircle():
    SCREEN.fill((0, 0, 255))

def gravity(y, speed):
    if(y < 350):
        y = y + speed
    return y

def jump(y, speed): 
    return y - speed

def moveRectangle(x, speed):
    return x - speed


size = (constants.SCREENHEIGHT, 400)
SCREEN = py.display.set_mode(size)

circle_y = constants.SCREENHEIGHT / 2

pipe_a = pipe.Pipe(constants.SCREENWIDTH, 250, True)
pipe_b = pipe.Pipe(constants.SCREENWIDTH, 250, False)

while True:
    
    for ev in py.event.get():
        if ev.type == py.QUIT:
            py.display.quit()
        if ev.type == py.KEYDOWN:
            if(ev.key ==  py.K_SPACE):
                circle_y = jump(circle_y, constants.JUMP_SPEED)
    
    createCircle()

    circle_y = gravity(circle_y, constants.GRAVITY_SPEED)

    py.draw.ellipse(SCREEN, (255, 255, 0), (50, circle_y, 50, 50))

    if(pipe_a.x < 0):
        pipe_a.x = constants.SCREENWIDTH
    
    if(pipe_b.x < 0):
        pipe_b.x = constants.SCREENWIDTH
    
    pipe_a.x = moveRectangle(pipe_a.x, constants.PIPE_SPEED)
    if(pipe_b.visible):
        py.draw.rect(SCREEN, (0, 128, 0), (pipe_b.x, pipe_b.y, pipe_b.width, pipe_b.height))
        pipe_b.x = moveRectangle(pipe_b.x, constants.PIPE_SPEED)

    if(pipe_a.x < constants.SCREENWIDTH/4 and not pipe_b.visible):
        pipe_b.visible = True
    
    py.draw.rect(SCREEN, (0, 128, 0), (pipe_a.x, pipe_a.y, pipe_a.width, pipe_a.height))
    py.display.update()



