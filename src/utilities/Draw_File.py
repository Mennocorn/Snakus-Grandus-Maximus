
from script.Point import V2
import datetime



class Drawing:

    def __init__(self, data, pygame):
        self.color = (255, 0, 0)
        self.sizes = data
        self.pygame = pygame

    def draw1(self, fps, head: V2, screen):

        # draw player
        screen.fill((0, 0, 0))

        self.pygame.draw.rect(screen, self.color, self.pygame.Rect(head.get_x(), head.get_y(), self.sizes.unit, self.sizes.unit))
        myfont = self.pygame.font.SysFont(None, 24)
        img = myfont.render(str(fps), True, (255, 255, 255))
        img2 = myfont.render(str(datetime.datetime.now()-self.sizes.start_time_timer), True, (255, 255, 255))
        screen.blit(img, (465, 480))
        screen.blit(img2, (10, 10))
        self.pygame.display.update()
        self.pygame.display.flip()

