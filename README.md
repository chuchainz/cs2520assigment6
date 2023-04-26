# CS2520 Assignment 6

Project is located under ----> Intro to Pygame Graphics > major league soccer animation > graphics_v4_vi18.py

draw_cloud(x, y): This function takes in the coordinates of the upper left corner of a cloud, and then draws the cloud using ellipses and rectangles.

draw_net(x, y): This function takes in the coordinates of the upper left corner of a soccer net, and then draws the net using lines and loops.

draw_light_pole(x, y): This function takes in the coordinates of the upper left corner of a light pole, and then draws the pole and its lights using rectangles, ellipses, and lines.

draw_field(x1, y1, x2, y2): This function draws the soccer field using rectangles, stripes, and loops. It takes in optional arguments to specify the coordinates of the field, but defaults to the entire screen width and the bottom 70% of the screen height.

draw_fence(y, height): This function draws a fence at a specified height on the screen using polygons and lines. It takes in optional arguments to specify the y-coordinate and height of the fence, but defaults to 170 and 15, respectively.

draw_scoreboard(x, y, width, height, pad): This function draws a scoreboard at a specified location and size using rectangles and lines. It takes in optional arguments to specify the x-coordinate, y-coordinate, width, height, and padding of the scoreboard, but defaults to 300, 40, 200, 90, and 2, respectively.

draw_stand: this function takes in a screen object, a list of stand_list which contains the coordinates for the left and right stands, and a colors_list which contains the colors of the stands. The function then uses the pygame.draw.polygon method to draw the stands on the screen with the corresponding colors. The stand1 and stand2 lists are the coordinates for the left and right stands, respectively.

draw_corner_flags: this function takes in the screen object, a color for the flag and a flag_pos which is the position where the flag is to be placed. The function then uses pygame.draw.line method to draw the pole of the flag and pygame.draw.polygon method to draw the flag with the given color.

added an updated version of graphics under graphics_v4_vi18.py



Members: Jimmy Chu (Chuchainz)
kelsey coen (potatosalad82)
