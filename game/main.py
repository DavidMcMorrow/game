import pygame as py
import constants
import pipe
import bird

def createCircle():
    SCREEN.fill((0, 0, 255))
    
def gravity(velocity):
    return velocity + constants.GRAVITY_SPEED

def jump(): 
    return -3

def moveRectangle(x, speed):
    return x - speed

game_clock = py.time.Clock()
game_fps = 60

size = (constants.SCREENHEIGHT, constants.SCREENWIDTH)
SCREEN = py.display.set_mode(size)

velocity = 0

pipe_a = pipe.Pipe(constants.SCREENWIDTH, 250, True)
pipe_b = pipe.Pipe(constants.SCREENWIDTH, 250, False)

bird = bird.Bird((constants.SCREENWIDTH / 4), (constants.SCREENHEIGHT / 2))

cycle = 0

while True:
    game_clock.tick(game_fps) 
    for ev in py.event.get():
        if ev.type == py.QUIT:
            py.display.quit()
        if ev.type == py.KEYDOWN:
            if(ev.key ==  py.K_SPACE):
                velocity = jump()
    
    createCircle()
    
    velocity = gravity(velocity)

    bird.y = bird.y + velocity

    py.draw.ellipse(SCREEN, (255, 255, 0), (bird.x, bird.y, 50, 50))

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

    cycle = cycle + 1



