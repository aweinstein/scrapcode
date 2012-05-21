import sys

import pygame
from pygame import Rect, Color

class Visualizer(object):
    def __init__(self, screen, field, messages):
        self.screen = screen
        self.field = field
        self.messages = messages

        self.field_color = Color('black')
        self.grid_color = Color('gray')
        self.cur_color = Color('red')
        self.goal_color = Color('green')
        self.wall_color = Color('gray')

        n = 11 # Environment is an n-by-n grid
        self.nrows, self.ncols = n, n
        self.grid_size = self.field.height / n

        self.goal = (10, 10)
        self.cur = (0, 0)
        
        rim_width = 4
        rim_color = Color('White')
        rim_rect = Rect(messages.left - rim_width,
                        messages.top - rim_width,
                        messages.width + rim_width * 2,
                        messages.height + rim_width * 2)
        pygame.draw.rect(screen, rim_color, rim_rect)
        pygame.draw.rect(screen, self.field_color, messages)

    def draw(self):
        self.draw_grid()
        self.draw_walls()
        self.draw_pos(self.goal, self.goal_color)
        self.draw_pos(self.cur, self.cur_color)

    def draw_grid(self):
        field = self.field
        self.screen.fill(self.field_color, field)

        for y in range(self.nrows + 1):
            ypos = field.top + y * self.grid_size - 1
            pygame.draw.line(self.screen,
                             self.grid_color,
                             (field.left, ypos),
                             (field.right - 1, ypos))

        for x in range(self.ncols + 1):
            xpos = field.left + x * self.grid_size -1
            pygame.draw.line(self.screen,
                             self.grid_color,
                             (xpos, field.top),
                             (xpos, field.bottom - 1))

    def draw_walls(self):
        # Walls defined as ((i,j), width, height)
        walls = (((0,5), 1, 1),
                 ((2,5), 3, 1),
                 ((5,0), 1, 2),
                 ((5,3), 1, 6),
                 ((6,6), 2, 1),
                 ((9,6), 2, 1),
                 ((5,10), 1, 1))
        
        for wall in walls:
            left = self.field.left + wall[0][0] * self.grid_size 
            top = self.field.top + wall[0][1] * self.grid_size
            width = wall[1] * self.grid_size - 1
            height = wall[2] * self.grid_size - 1
            #print left, top, width, height
            self.screen.fill(self.wall_color, Rect(left, top, width, height))

    def draw_pos(self, (i, j), color):
        field = self.field
        pos_x = field.left + j * self.grid_size + self.grid_size / 2
        pos_y = field.top + i * self.grid_size + self.grid_size / 2
        radius = self.grid_size / 4

        pygame.draw.circle(self.screen, color, (pos_x, pos_y), radius)

def draw_rimmed_box(screen, box_rect, box_color, 
                    rim_width=0, 
                    rim_color=Color('black')):
    """ Draw a rimmed box on the given surface. The rim is drawn
        outside the box rect.
    """
    if rim_width:
        rim_rect = Rect(box_rect.left - rim_width,
                        box_rect.top - rim_width,
                        box_rect.width + rim_width * 2,
                        box_rect.height + rim_width * 2)
        pygame.draw.rect(screen, rim_color, rim_rect)
    
    pygame.draw.rect(screen, box_color, box_rect)

if __name__ == '__main__':
    w = 297
    FIELD_RECT = Rect(25, 25, w, w)
    MESSAGES_RECT = Rect(25, FIELD_RECT.h + 50, w, 75)
    SCREEN_WIDTH = w + 50
    SCREEN_HEIGHT =  FIELD_RECT.h + MESSAGES_RECT.h + 75

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    clock = pygame.time.Clock()
        
    visualizer = Visualizer(screen, FIELD_RECT, MESSAGES_RECT)

    k = 0
    while True:
        time_passed = clock.tick(10)
        k += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        if (k % 10) == 0:
            visualizer.cur = visualizer.cur[0] + 1, visualizer.cur[1] + 1
        visualizer.draw()
       
        pygame.display.flip()
