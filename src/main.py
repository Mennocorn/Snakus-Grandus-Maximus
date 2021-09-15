import pygame, time
from pygame.locals import *
import keyboard
from script.Point import V2
import datetime
from script.Obstruction import Apple
from utilities.timer import Timer
from utilities.Draw_File import Drawing


class GameData:
    def __init__(self):
        self.x = 500
        self.y = 500
        self.unit = 25
        self.fps = 0
        self.current_fps = 0
        # mainloop settings
        self.running = True
        self.speed = 0.00001
        self.current = time.time()
        self.direction = "DOWN"
        self.movement_speed = 0.3
        self.start_time = time.time()
        self.start_time_timer = datetime.datetime.now()

data = GameData()
pygame.init()
screen = pygame.display.set_mode((data.x, data.y))
pygame.display.set_caption('Cooles Game, pre pre pre alpha -1')
pygame.mouse.set_visible(False)

BLUE = (0, 0, 255)

screen.fill(BLUE)
pygame.draw.rect(screen, BLUE, (200, 150, 100, 50))



head = V2(100, 100)
body = []

x_draw = Drawing(data, pygame)



# food
food = Apple()
YELLOW = (255, 255, 51)





    #    i = 1
#    for i in range(i < data.x / data.unit):
#        pygame.draw.line(screen, YELLOW, [i * data.unit, 0], [i * data.unit, data.y])
#        pygame.draw.line(screen, YELLOW, [0, i * data.unit], [data.x, i * data.unit])

#        i += 1
    



def tick():
    

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # handle input

    if keyboard.is_pressed('w') and data.direction != "DOWN":
        data.direction = "UP"
    elif keyboard.is_pressed('s') and data.direction != "UP":
        data.direction = "DOWN"
    elif keyboard.is_pressed('a') and data.direction != "RIGHT":
        data.direction = "LEFT"
    elif keyboard.is_pressed('d') and data.direction != "LEFT":
        data.direction = "RIGHT"

    # move snake

    if data.direction == "UP":
        head.set_y(head.get_y() - data.movement_speed)
    elif data.direction == "DOWN":
        head.set_y(head.get_y() + data.movement_speed)
    elif data.direction == "LEFT":
        head.set_x(head.get_x() - data.movement_speed)
    elif data.direction == "RIGHT":
        head.set_x(head.get_x() + data.movement_speed)



    # check collision
    # # pos = food[i]
    # if pos.get_x() < head.get_x() + data.unit and pos.get_x() + data.unit > head.get_x():
    #     if pos.get_y() < head.get_y() + data.unit and pos.get_y() + data.unit > head.get_x():
    #         print("Jaa es funktioniert")
    #         # create new food
    # # check border


def check_collision():
    x = head.get_x()
    y = head.get_y()

    if head.get_x() < 0 or head.get_x() + data.unit > data.x or head.get_y() + data.unit > data.y or head.get_y() < 0:

        pygame.quit()
        print(f"out x: {x}, y: {y}, x_size: {data.x}, y_size: {data.y}")



movement_timer = Timer(data.speed)
font_timer = Timer(1)
pygame.font.init()





while data.running:
    # generating fps
    now = time.time()
    data.current_fps += 1
    if now - data.start_time > 1:
        data.start_time = now
        data.fps = data.current_fps
        data.current_fps = 0
    if movement_timer.elapsed():

        tick()


        check_collision()
    x_draw.draw1(data.fps, head, screen)





