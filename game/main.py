import pygame as py
import constants
import pipe
import bird as flight
import random
import sys

# https://www.pixilart.com/draw?ref=home-page - To create bird, pipes background

def createScreen():
    SCREEN.fill(constants.BACKGROUND_COLOUR)
    
def gravity(velocity):
    return velocity + constants.GRAVITY_SPEED

def jump(): 
    return constants.JUMP_SPEED

def deathFlinch():
    return constants.DEATH_SPEED

def createPipe(startX):
    random_height = random.randint(150, constants.SCREEN_HEIGHT - 150)
    pipe_bottom = pipe.Pipe(startX, random_height, constants.SCREEN_HEIGHT - random_height, None)
    pipe_top = pipe.Pipe(startX, 0, random_height - 150, None)
    return (pipe_bottom, pipe_top)

def hitDetection(bird, pipe_A_bot, pipe_B_bot, pipe_A_top, pipe_B_top):
    result = False
    if(hitScreenEdge(bird.y)):
        result = True

    if(hitPipe(bird, pipe_A_bot) or hitPipe(bird, pipe_B_bot) or hitPipe(bird, pipe_a_top) or hitPipe(bird, pipe_b_top)):
        result = True
    
    return result

def hitScreenEdge(y):
    return (y <= 0 or y + 50 >= constants.SCREEN_HEIGHT)

def hitPipe(bird, bottom_pipe):
    if(bottom_pipe.rect.colliderect(bird.circle)):
        return True

def setupGame():
    (pipe_a_bottom, pipe_a_top) = createPipe((constants.SCREEN_WIDTH * 2))
    (pipe_b_bottom, pipe_b_top)  = createPipe((constants.SCREEN_WIDTH * 2.5))
    bird = flight.Bird((constants.SCREEN_WIDTH / 4), (constants.SCREEN_HEIGHT / 2), True, None)
    bird_colour = constants.BIRD_NATURAL_COLOUR
    velocity = 0
    return (velocity, bird_colour, bird, pipe_a_bottom, pipe_a_top, pipe_b_bottom, pipe_b_top)

def determiningBirdColour(bird):
    result = constants.BIRD_NATURAL_COLOUR
    if(not bird.alive):
        result = constants.BIRD_DEAD_COLOUR
    return result 
    

game_clock = py.time.Clock()
game_fps = 60

size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
SCREEN = py.display.set_mode(size)

(velocity, bird_colour, bird, pipe_a_bottom, pipe_a_top, pipe_b_bottom, pipe_b_top) = setupGame()

cycle = 0

while True:
    game_clock.tick(game_fps) 
    for ev in py.event.get():
        if ev.type == py.QUIT:
            py.display.quit()
        if ev.type == py.KEYDOWN:
            if(ev.key ==  py.K_SPACE):
                velocity = jump()
    
    createScreen()
    
    velocity = gravity(velocity)

    bird.y = bird.y + velocity

    bird.circle = py.draw.ellipse(SCREEN, determiningBirdColour(bird), (bird.x, bird.y, 50, 50))


    if(pipe_a_bottom.x < 0):
        (pipe_a_bottom, pipe_a_top) = createPipe(constants.SCREEN_WIDTH )
        
    if(pipe_b_bottom.x < 0):
        (pipe_b_bottom, pipe_b_top) = createPipe(constants.SCREEN_WIDTH)
    
    pipe_a_bottom.rect = py.draw.rect(SCREEN, constants.PIPE_COLOUR, (pipe_a_bottom.x, pipe_a_bottom.y, pipe_a_bottom.width, pipe_a_bottom.height))
    pipe_a_top.rect = py.draw.rect(SCREEN, constants.PIPE_COLOUR, (pipe_a_top.x, pipe_a_top.y, pipe_a_top.width, pipe_a_top.height))

    pipe_b_bottom.rect = py.draw.rect(SCREEN, constants.PIPE_COLOUR, (pipe_b_bottom.x, pipe_b_bottom.y, pipe_b_bottom.width, pipe_b_bottom.height)) 
    pipe_b_top.rect = py.draw.rect(SCREEN, constants.PIPE_COLOUR, (pipe_b_top.x, pipe_b_top.y, pipe_b_top.width, pipe_b_top.height)) 

    if(bird.alive):
        (pipe_a_bottom, pipe_b_bottom, pipe_a_top, pipe_b_top) = pipe.moveAllRectangles(pipe_a_bottom, pipe_b_bottom, pipe_a_top, pipe_b_top)
        if(hitDetection(bird, pipe_a_bottom, pipe_b_bottom, pipe_a_top, pipe_b_top)):
            bird.alive = False
            velocity = deathFlinch() 
    
    else:
        if(hitScreenEdge(bird.y)):
            py.display.quit()
            sys.exit()
        
    
    py.display.update()

    cycle = cycle + 1

    
        