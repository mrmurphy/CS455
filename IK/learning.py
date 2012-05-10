import bge
from math import *


def main():

    cont = bge.logic.getCurrentController()
    player = cont.owner
    keyboard = bge.logic.keyboard
    factor = 0.4
    rotFactor = 0.05
    mouse = bge.logic.mouse
    height = bge.render.getWindowHeight()
    width = bge.render.getWindowWidth()
    suzy = bge.logic.getCurrentScene().objects['Monkey']

    amp = 10 
    per = 5
    newY = amp * cos( 2 * pi / 5 * player['timer'])
    player.worldPosition = (player.position[0], newY, 0)

main()