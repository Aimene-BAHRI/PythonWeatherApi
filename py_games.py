import pygame as pg
# Import py_api.py file 
import py_api

# Initialize all modales from pygame
pg.init()

# Add a font monoscape with a size of 15
myfont = pg.font.SysFont("monospace", 15)
# Create a sxcreen show with a 400 width and 300 height
screen = pg.display.set_mode((400, 300))

done = False

x = 30
y = 30

# Get tempurature from py_api.py file that was import befor
temp = py_api.temp()

# make some test of tempurature and change the icon dynamicly
if temp < 10 : img = pg.image.load('./images/WeatherIcons/41.png')
elif temp > 10 <= 20 : img = pg.image.load('./images/WeatherIcons/34.png')
elif temp > 20 <= 30 : img = pg.image.load('./images/WeatherIcons/36.png')

while not done:
    # Listening for events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    screen.fill((0, 0, 0))
    
    # Add an output text
    label = myfont.render('Temp:{0} C'.format(temp), 1, (255,255,0))
    screen.blit(img ,(8,8))
    screen.blit(label, (150, 150))
    pg.display.flip()
