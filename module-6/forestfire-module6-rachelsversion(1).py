#Red Team
#Module 6
#CSD 325
#11.20.24

#This program is a modified version of Sue Sampson's Forest Fire Sim that has been changed to include a lake

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
LAKE = '~' #adding lake constant 
EMPTY = ' '

INITIAL_TREE_DENSITY = 0.20  
GROW_CHANCE = 0.01  
FIRE_CHANCE = 0.01  
PAUSE_LENGTH = 0.5

def main():
    forest = createNewForest()
    bext.clear()

    while True:
        displayForest(forest)

        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    continue
                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    nextForest[(x, y)] = EMPTY
                else:
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)


def createNewForest():
    
    forest = {'width': WIDTH, 'height': HEIGHT}

    #initialize lake
    lake_width = 15
    lake_height = 7
    lake_center_x = WIDTH // 2
    lake_center_y = HEIGHT // 2

    # Define the lake's position within the plot
    lake_left = lake_center_x - lake_width // 2
    lake_right = lake_center_x + lake_width // 2
    lake_top = lake_center_y - lake_height // 2
    lake_bottom = lake_center_y + lake_height // 2

    for x in range(WIDTH):
        for y in range(HEIGHT):

            if lake_left <= x <= lake_right and lake_top <= y <= lake_bottom:
                forest[(x, y)] = LAKE  #adding lake to plot
            elif (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  
            else:
                forest[(x, y)] = EMPTY  

    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(x, y)] == LAKE:
                bext.fg('blue') #coloring lake character blue
                print(LAKE, end='') #display lake
                
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()

    bext.fg('reset') 
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() 

#References
#Canyoning.Cat. (2013, December 23). Pygame Part 3 – Velocity/Movement and Bounding Boxes. Eclecticcats.
#https://eclecticcats.wordpress.com/2013/12/23/pygame-part-3-velocitymovement-and-bounding-boxes/