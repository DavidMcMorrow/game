import constants

class Pipe:
    def __init__(pipe, x, y, height, rectangle):
        pipe.x = x
        pipe.y = y
        pipe.width = constants.PIPE_WIDTH
        pipe.height = height
        pipe.rect = rectangle

def moveRectangle(x, speed):
    return x - speed

def moveAllRectangles(pipe_a_bottom, pipe_b_bottom, pipe_a_top, pipe_b_top):
    pipe_a_bottom.x = moveRectangle(pipe_a_bottom.x, constants.PIPE_SPEED)
    pipe_a_top.x = moveRectangle(pipe_a_top.x, constants.PIPE_SPEED)

    pipe_b_bottom.x = moveRectangle(pipe_b_bottom.x, constants.PIPE_SPEED)
    pipe_b_top.x = moveRectangle(pipe_b_top.x, constants.PIPE_SPEED)

    return (pipe_a_bottom, pipe_b_bottom, pipe_a_top, pipe_b_top)

    
