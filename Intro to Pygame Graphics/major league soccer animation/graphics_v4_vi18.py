"""This version of the graphics.py shows a demo soccer field for use in a
future game.
CS 2520 Assignment 6 refactoring project
"""

# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
width = SIZE[0]
height = SIZE[1]
TITLE = "Major League Soccer"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
''' add colors you use as RGB values here '''
RED = (255, 0, 0)
GREEN = (52, 166, 36)
BLUE = (29, 116, 248)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
DARK_BLUE = (18, 0, 91)
DARK_GREEN = (0, 94, 0)
GRAY = (130, 130, 130)
YELLOW = (255, 255, 110)
SILVER = (200, 200, 200)
DAY_GREEN = (41, 129, 29)
NIGHT_GREEN = (0, 64, 0)
BRIGHT_YELLOW = (255, 244, 47)
NIGHT_GRAY = (104, 98, 115)
ck = (127, 33, 33)
DARK = BLACK
THROUGH = (124, 118, 135)

# Alpha values
DARK_ALPHA = 200
THROUGH_ALPHA = 150

# Backgrounds
DARKNESS = pygame.Surface(SIZE)
DARKNESS.set_alpha(DARK_ALPHA)
DARKNESS.fill(DARK)

SEE_THROUGH = pygame.Surface((width, round(height*0.3)))
SEE_THROUGH.set_alpha(THROUGH_ALPHA)
SEE_THROUGH.fill(THROUGH)

# Constants in code (from magic numbers)
NUMBER_STARS = 200
NUMBER_CLOUDS = 20

MIN_STAR_RAD = 1
MAX_STAR_RAD = 2
STAR_REGION = 1/3

MIN_CLOUD_POS = -1/8
MAX_CLOUD_POS = 2
CLOUD_REGION = 1/4
CLOUD_SPEED = 0.5

FIELD_LEVEL = 0.3

## Functions
def draw_cloud(x, y):
    """Draw a cloud with the upper left corner at coordinates (x, y)."""
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x, y + 8, 10, 10])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 6, y + 4, 8, 8])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 10, y, 16, 16])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 20, y + 8, 10, 10])
    pygame.draw.rect(SEE_THROUGH, cloud_color, [x + 6, y + 8, 18, 10])

def draw_net(x, y):
    """Draw a net with the upper left corner at coordinates (x, y)."""
    #net
    offset_x1 = (list(range(5, 40, 5)) + list(range(40, 120, 4))
                         + list(range(120, 160, 5)))
    offset_x2 = (list(range(21, 45, 3)) + list(range(45, 60, 4))
                         + list(range(60, 103, 4)) + list(range(103, 115, 4))
                         + list(range(115, 140, 3)))
    for x1, x2 in zip(offset_x1, offset_x2):
        pygame.draw.line(screen, WHITE, [x+x1, y], [x+x2, y+60], 1)

    #net part 2 and 3
    for x1 in (0, 160):
        for y2 in range(76, 60, -2):
            x_offset = 80-y2
            if x1 > 80: x_offset *= -1
            pygame.draw.line(screen, WHITE, [x+x1, y], [x+x1+x_offset, y+y2], 1)

    #net part 4
    for offset in range(4, 60, 4):
        if y < 40:
            x1 = 4
            x2 = 156
        else:
            x1 = 15
            x2 = 145
            if offset == 40:
                x2 += 5
        pygame.draw.line(screen, WHITE, [x+x1, y+offset], [x+x2, y+offset], 1)

def draw_light_pole(x, y):
    """Draw a light pole with the upper left corner at coordinates (x, y)."""
    y_offset = 40
    interval = 20
    width = 100
    pygame.draw.rect(screen, GRAY, [x+40, y+y_offset, interval, 140])
    pygame.draw.ellipse(screen, GRAY, [x+40, y+175, interval, 10])

    #lights
    pygame.draw.line(screen, GRAY, [x, y+y_offset], [x+width, y+y_offset], 2)
    for offset in range(0, y_offset, interval):
        for x_offset in range(0, width, interval):
            pygame.draw.ellipse(screen, light_color, [x+x_offset, y+offset,
                                                      interval, interval])
        pygame.draw.line(screen, GRAY, [x, y+offset], [x+x_offset+20, y+offset], 2)

def draw_field(x1=0, y1=round(FIELD_LEVEL * height), x2=width, y2=height):
    """Draw the field with the coordinates specified.
    Defaults to the entire screen width and bottom 70% of the screen height.
    """
    y_len = y2-y1
    pygame.draw.rect(screen, field_color, [x1, y1, x2-x1, y_len])
    curr_y = y1
    perspective = 42
    while curr_y < y2:
        pygame.draw.rect(screen, stripe_color, [x1, curr_y, x2-x1, perspective])
        curr_y += 2 * perspective
        if curr_y < round(0.75 * height):
            perspective += 10
        else:
            perspective += 20

def draw_fence(y=170, height=15):
    """Draw a fence at the specified y coordinate with specified height."""
    for x in range(5, width, 30):
        pygame.draw.polygon(screen, NIGHT_GRAY, [[x + 2, y], [x + 2, y+height],
                                                 [x, y+height], [x, y]])
    for x in range(5, width, 3):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x, y+height], 1)

    for fence_line in range(y, y+height, 4):
        pygame.draw.line(screen, NIGHT_GRAY, [0, fence_line],
                         [width, fence_line], 1)

def draw_scoreboard(x=300, y=40, width=200, height=90, pad=2):
    """Draw the scoreboard with the upper left corner at coordinates (x, y)."""
    pole_width = 20
    pole_height = 70
    pygame.draw.rect(screen, GRAY, [x + (width-pole_width)//2, y + height - 10,
                                    pole_width, pole_height])
    pygame.draw.rect(screen, BLACK, [x, y, width, height])
    pygame.draw.rect(screen, WHITE, [x, y, width, height], 2)

# Config
lights_on = True
day = True

stars = []
for n in range(NUMBER_STARS):
    x = random.randrange(0, width)
    y = random.randrange(0, round(height*STAR_REGION))
    r = random.randrange(MIN_STAR_RAD, MAX_STAR_RAD)
    stars.append([x, y, r, r])

clouds = []
for i in range(NUMBER_CLOUDS):
    x = random.randrange(round(width * MIN_CLOUD_POS), 2 * MAX_CLOUD_POS)
    y = random.randrange(0, round(height*CLOUD_REGION))
    clouds.append([x, y])
    
# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                lights_on = not lights_on
            elif event.key == pygame.K_d:
                day = not day

    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now '''
    #lights turn on and off now
    if not day:
        light_color = YELLOW
    else:
        light_color = SILVER

    if day:
        sky_color = BLUE
        field_color = GREEN
        stripe_color = DAY_GREEN
        cloud_color = WHITE
        
    else:
        sky_color = DARK_BLUE
        field_color = DARK_GREEN
        stripe_color = NIGHT_GREEN
        cloud_color = NIGHT_GRAY

    for c in clouds:
        c[0] -= CLOUD_SPEED

        if c[0] < width * MIN_CLOUD_POS:
            c[0] = random.randrange(width, 2 * width)
            c[1] = random.randrange(0, round(height*CLOUD_REGION))
            
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(sky_color)
    SEE_THROUGH.fill(ck)
    SEE_THROUGH.set_colorkey(ck)
    
    if not day:
        #stars are only shown at night
        for s in stars:
            pygame.draw.ellipse(screen, WHITE, s)

    draw_field(0, 180, 800, 600)
    draw_fence(170, 15)

    # The sun and sky
    if day:
        pygame.draw.ellipse(screen, BRIGHT_YELLOW, [520, 50, 40, 40])
    else:
        pygame.draw.ellipse(screen, WHITE, [520, 50, 40, 40]) 
        pygame.draw.ellipse(screen, sky_color, [530, 45, 40, 40])

    # draw the clouds
    for c in clouds:
        draw_cloud(c[0], c[1])
    screen.blit(SEE_THROUGH, (0, 0))   
    
    #out of bounds lines
    pygame.draw.line(screen, WHITE, [0, 580], [800, 580], 5)
    #left
    pygame.draw.line(screen, WHITE, [0, 360], [140, 220], 5)
    pygame.draw.line(screen, WHITE, [140, 220], [660, 220], 3)
    #right
    pygame.draw.line(screen, WHITE, [660, 220], [800, 360], 5)

    #safety circle
    pygame.draw.ellipse(screen, WHITE, [240, 500, 320, 160], 5)

    #18 yard line goal box
    pygame.draw.line(screen, WHITE, [260, 220], [180, 300], 5)
    pygame.draw.line(screen, WHITE, [180, 300], [620, 300], 3)
    pygame.draw.line(screen, WHITE, [620, 300], [540, 220], 5)

    #arc at the top of the goal box
    pygame.draw.arc(screen, WHITE, [330, 280, 140, 40], math.pi, 2 * math.pi, 5)

    draw_scoreboard(300, 40, 200, 90)

    #goal
    pygame.draw.rect(screen, WHITE, [320, 140, 160, 80], 5)
    pygame.draw.line(screen, WHITE, [340, 200], [460, 200], 3)
    pygame.draw.line(screen, WHITE, [320, 220], [340, 200], 3)
    pygame.draw.line(screen, WHITE, [480, 220], [460, 200], 3)
    pygame.draw.line(screen, WHITE, [320, 140], [340, 200], 3)
    pygame.draw.line(screen, WHITE, [480, 140], [460, 200], 3)

    #6 yard line goal box
    pygame.draw.line(screen, WHITE, [310, 220], [270, 270], 3)
    pygame.draw.line(screen, WHITE, [270, 270], [530, 270], 2)
    pygame.draw.line(screen, WHITE, [530, 270], [490, 220], 3)
    
    #light pole 1 and 2
    draw_light_pole(110, 20)
    draw_light_pole(590, 20)

    # net
    draw_net(320, 140)

    #This method takes in coordinates and colors as arguements to make the stands in the screen
    def draw_stand(screen, stand_list, colors_list):
        for i in range(len(stand_list)):
            pygame.draw.polygon(screen, colors_list[i], stand_list[i])
    
    #coordinate lists to make the right and left stands
    stand1 = [[[680, 220], [800, 340], [800, 290], [680, 180]], 
              [[680, 180], [800, 100], [800, 290]]]
    stand2 = [[[120, 220], [0, 340], [0, 290], [120, 180]], 
              [[120, 180], [0, 100], [0, 290]]]
    color_list = [RED, WHITE]

    #implementation of the method to output the stand on the screen 
    draw_stand(screen, stand1, color_list)
    draw_stand(screen, stand2, color_list)

    #This method takes in color and flag coordinates as arguements to make the flags in the screen.
    def draw_corner_flags(screen, color, flag_pos):
        pygame.draw.line(screen, BRIGHT_YELLOW, flag_pos, (flag_pos[0]-5, flag_pos[1]-30), 3)
        pygame.draw.polygon(screen, color, [(flag_pos[0]-8, flag_pos[1]-30), (flag_pos[0]-15, flag_pos[1]-24), (flag_pos[0]-5, flag_pos[1]-15)])

    #implentation of the method with coordinates to output the flats on the screen
    draw_corner_flags(screen, RED, (140, 220))  # draw right corner flag
    draw_corner_flags(screen, RED, (660, 220))  # draw left corner flag

    # DARKNESS
    if not day and not lights_on:
        screen.blit(DARKNESS, (0, 0))    
    
    #pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()

    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)

# Close window and quit
pygame.quit()
