# Author : Zeeshan khalid
# Here Is Are Apple Made
import random
from config import Config


class Apple():
    def __init__(self, snake):
        self.setNewLocation(snake)

    def setNewLocation(self, snake):
        while True:
            x = random.randint(0, Config.CELLWIDTH - 1)
            y = random.randint(0, Config.CELLHEIGHT - 1)
            if not self.inSnakeBody(x, y, snake):
                break

            print("OOPS. almost put an apple in the snake :p")

        self.x = x
        self.y = y

    def inSnakeBody(self, x, y, snake):
        for coord in snake.wormCoords:
            if coord['x'] == x and coord['y'] == y:
                return True

        return False
