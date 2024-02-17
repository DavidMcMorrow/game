import pygame as py
import constants
import pipe
import bird
import random

# https://www.pixilart.com/draw?ref=home-page - To create bird, pipes background

def createCircle():
    SCREEN.fill((0, 0, 255))
    
def gravity(velocity):
    return velocity + constants.GRAVITY_SPEED

def jump(): 
    return -3

def moveRectangle(x, speed):
    return x - speed

def createPipe(startX):
    random_height = random.randint(150, constants.SCREENHEIGHT - 150)
    pipe_bottom = pipe.Pipe(startX, random_height, 50, constants.SCREENHEIGHT - random_height)
    pipe_top = pipe.Pipe(startX, 0, 50, random_height - 150)
    return (pipe_bottom, pipe_top)

game_clock = py.time.Clock()
game_fps = 60

size = (constants.SCREENWIDTH, constants.SCREENHEIGHT)
SCREEN = py.display.set_mode(size)

velocity = 0

(pipe_a_bottom, pipe_a_top) = createPipe((constants.SCREENWIDTH * 2))
(pipe_b_bottom, pipe_b_top)  = createPipe((constants.SCREENWIDTH * 2.5))

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

    if(pipe_a_bottom.x < 0):
        (pipe_a_bottom, pipe_a_top) = createPipe(constants.SCREENWIDTH )
    
    if(pipe_b_bottom.x < 0):
        (pipe_b_bottom, pipe_b_top) = createPipe(constants.SCREENWIDTH)
    
    py.draw.rect(SCREEN, (44, 176, 26), (pipe_a_bottom.x, pipe_a_bottom.y, pipe_a_bottom.width, pipe_a_bottom.height))
    py.draw.rect(SCREEN, (44, 176, 26), (pipe_a_top.x, pipe_a_top.y, pipe_a_top.width, pipe_a_top.height))
    
    py.draw.rect(SCREEN, (44, 176, 26), (pipe_b_bottom.x, pipe_b_bottom.y, pipe_b_bottom.width, pipe_b_bottom.height)) # magenta
    py.draw.rect(SCREEN, (44, 176, 26), (pipe_b_top.x, pipe_b_top.y, pipe_b_top.width, pipe_b_top.height)) # magenta

    pipe_a_bottom.x = moveRectangle(pipe_a_bottom.x, constants.PIPE_SPEED)
    pipe_a_top.x = moveRectangle(pipe_a_top.x, constants.PIPE_SPEED)
    
    pipe_b_bottom.x = moveRectangle(pipe_b_bottom.x, constants.PIPE_SPEED)
    pipe_b_top.x = moveRectangle(pipe_b_top.x, constants.PIPE_SPEED)
    
    py.display.update()

    cycle = cycle + 1
