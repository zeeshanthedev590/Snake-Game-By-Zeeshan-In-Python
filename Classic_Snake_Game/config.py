# Author : Zeeshan Khalid
# This Is A V.VIP File So If You Need To Change Somthing In The Game So Change In This File
class Config():
    FPS = 15
    MENU_FPS = 200
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    CELLSIZE = 20
    assert WINDOW_WIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
    assert WINDOW_HEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
    CELLWIDTH = int(WINDOW_WIDTH / CELLSIZE)
    CELLHEIGHT = int(WINDOW_HEIGHT / CELLSIZE)

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0,   0,   0)
    RED = (255,   0,   0)
    GREEN = (0, 255,   0)
    DARKGREEN = (0, 155,   0)
    DARKGRAY = (40,  40,  40)
    BG_COLOR = BLACK
