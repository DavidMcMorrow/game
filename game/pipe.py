import constants

class Pipe:
    def __init__(pipe, x, y, visible):
        pipe.x = x
        pipe.y = y
        pipe.width = 50
        pipe.height = constants.SCREENHEIGHT - y
        pipe.visible = visible




        

    
