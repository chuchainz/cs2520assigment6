# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
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

DARKNESS = pygame.Surface(SIZE)
DARKNESS.set_alpha(200)
DARKNESS.fill((0, 0, 0))

SEE_THROUGH = pygame.Surface((800, 180))
SEE_THROUGH.set_alpha(150)
SEE_THROUGH.fill((124, 118, 135))

def draw_cloud(x, y):
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x, y + 8, 10, 10])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 6, y + 4, 8, 8])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 10, y, 16, 16])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 20, y + 8, 10, 10])
    pygame.draw.rect(SEE_THROUGH, cloud_color, [x + 6, y + 8, 18, 10])


# Config
lights_on = True
day = True

stars = []
for n in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 200)
    r = random.randrange(1, 2)
    stars.append([x, y, r, r])

clouds = []
for i in range(20):
    x = random.randrange(-100, 1600)
    y = random.randrange(0, 150)
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
    if lights_on:
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
        c[0] -= 0.5

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 150)
            
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(sky_color)
    SEE_THROUGH.fill(ck)
    SEE_THROUGH.set_colorkey(ck)
    
    if not day:
    #stars
        for s in stars:
            pygame.draw.ellipse(screen, WHITE, s)




    pygame.draw.rect(screen, field_color, [0, 180, 800 , 420])
    pygame.draw.rect(screen, stripe_color, [0, 180, 800, 42])
    pygame.draw.rect(screen, stripe_color, [0, 264, 800, 52])
    pygame.draw.rect(screen, stripe_color, [0, 368, 800, 62])
    pygame.draw.rect(screen, stripe_color, [0, 492, 800, 82])


    '''fence'''
    y = 170
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, NIGHT_GRAY, [[x + 2, y], [x + 2, y + 15], [x, y + 15], [x, y]])

    y = 170
    for x in range(5, 800, 3):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x, y + 15], 1)

    x = 0
    for y in range(170, 185, 4):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x + 800, y], 1)

    if day:
        pygame.draw.ellipse(screen, BRIGHT_YELLOW, [520, 50, 40, 40])
    else:
        pygame.draw.ellipse(screen, WHITE, [520, 50, 40, 40]) 
        pygame.draw.ellipse(screen, sky_color, [530, 45, 40, 40])

    
    
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
    
    #score board pole
    pygame.draw.rect(screen, GRAY, [390, 120, 20, 70])

    #score board
    pygame.draw.rect(screen, BLACK, [300, 40, 200, 90])
    pygame.draw.rect(screen, WHITE, [302, 42, 198, 88], 2)


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

    #light pole 1
    pygame.draw.rect(screen, GRAY, [150, 60, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [150, 195, 20, 10])

    #lights
    pygame.draw.line(screen, GRAY, [110, 60], [210, 60], 2)
    pygame.draw.ellipse(screen, light_color, [110, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [130, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [150, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [170, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [190, 40, 20, 20])
    pygame.draw.line(screen, GRAY, [110, 40], [210, 40], 2)
    pygame.draw.ellipse(screen, light_color, [110, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [130, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [150, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [170, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [190, 20, 20, 20])
    pygame.draw.line(screen, GRAY, [110, 20], [210, 20], 2)

    #light pole 2
    pygame.draw.rect(screen, GRAY, [630, 60, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [630, 195, 20, 10])

    #lights

        
    pygame.draw.line(screen, GRAY, [590, 60], [690, 60], 2)
    pygame.draw.ellipse(screen, light_color, [590, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [610, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [630, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [650, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [670, 40, 20, 20])
    pygame.draw.line(screen, GRAY, [590, 40], [690, 40], 2)
    pygame.draw.ellipse(screen, light_color, [590, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [610, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [630, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [650, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [670, 20, 20, 20])
    pygame.draw.line(screen, GRAY, [590, 20], [690, 20], 2)

    #This method makes takes in coordinates for the color, points, and width as arguements to make the goal in the screen
    def draw_net(screen, color, points_list, width):
        for points in points_list:
            pygame.draw.line(screen, color, points[0], points[1], width)
    
    #these are coordinates to make the net and can be changed when needed
    net1 = [([325, 140], [341, 200]), 
            ([330, 140], [344, 200]), 
            ([335, 140], [347, 200]),
            ([340, 140], [350, 200]),
            ([345, 140], [353, 200]),
            ([350, 140], [356, 200]),
            ([355, 140], [359, 200]),
            ([360, 140], [362, 200]),
            ([364, 140], [365, 200]),
            ([368, 140], [369, 200]),
            ([372, 140], [373, 200]),
            ([376, 140], [377, 200]),
            ([380, 140], [380, 200]),
            ([384, 140], [384, 200]),
            ([388, 140], [388, 200]),
            ([392, 140], [392, 200]),
            ([396, 140], [396, 200]),
            ([400, 140], [400, 200]),
            ([404, 140], [404, 200]),
            ([408, 140], [408, 200]),
            ([412, 140], [412, 200]),
            ([416, 140], [416, 200]),
            ([420, 140], [420, 200]),
            ([424, 140], [423, 200]),
            ([428, 140], [427, 200]),
            ([432, 140], [431, 200]),
            ([436, 140], [435, 200]),
            ([440, 140], [438, 200]),
            ([445, 140], [441, 200]),
            ([450, 140], [444, 200]),
            ([455, 140], [447, 200]),
            ([460, 140], [450, 200]),
            ([465, 140], [453, 200]),
            ([470, 140], [456, 200]),
            ([475, 140], [459, 200])]
    
    net2 = [([320, 140], [324, 216]),
            ([320, 140], [326, 214]),
            ([320, 140], [328, 212]),
            ([320, 140], [330, 210]),
            ([320, 140], [332, 208]),
            ([320, 140], [334, 206]),
            ([320, 140], [336, 204]),
            ([320, 140], [338, 202])]
    
    net3 = [([480, 140], [476, 216]),
            ([480, 140], [474, 214]),
            ([480, 140], [472, 212]),
            ([480, 140], [470, 210]),
            ([480, 140], [468, 208]),
            ([480, 140], [466, 206]),
            ([480, 140], [464, 204]),
            ([480, 140], [462, 202])]
    
    net4 = [([324, 144], [476, 144]),
            ([324, 148], [476, 148]),
            ([324, 152], [476, 152]),
            ([324, 156], [476, 156]),
            ([324, 160], [476, 160]),
            ([324, 164], [476, 164]),
            ([324, 168], [476, 168]),
            ([324, 172], [476, 172]),
            ([324, 176], [476, 176]),
            ([335, 180], [470, 180]),
            ([335, 184], [465, 184]),
            ([335, 188], [465, 188]),
            ([335, 192], [465, 192]),
            ([335, 196], [465, 196])]

    #call the methods to actually make the net using all 4 coordinate lists
    draw_net(screen, WHITE, net1, 1)
    draw_net(screen, WHITE, net2, 1)
    draw_net(screen, WHITE, net3, 1)
    draw_net(screen, WHITE, net4, 1)

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
