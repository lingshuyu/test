import pygame
import random

pygame.init()

pic = pygame.image.load('raining.jpg')
screen_width = pic.get_width()
screen_height = pic.get_height()
screen = pygame.display.set_mode([screen_width, screen_height])
numbers = 50
colors = [0] * numbers
location_x = [0] * numbers
location_y = [0] * numbers
sizes = [0] * numbers
speed = [0] * numbers

for i in range(numbers):
    colors[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    location_x[i] = random.randint(0, screen_width)
    location_y[i] = random.randint(0, screen_height)
    sizes[i] = random.randint(5, 20)
    speed[i] = random.randint(1, 5)
    keep_going = True

timer = pygame.time.Clock()
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

screen.blit(pic, (0, 0))
for i in range(numbers):
    pygame.draw.circle(screen, colors[i], (location_x[i], location_y[i], sizes[i]))
    location_y[i] = location_y[i] + speed[i]
    if location_y[i] > screen_height:
        location_y[i] -= screen_height
        location_x[i] = random.randint(0, screen_width)
        speed[i] = random.randint(1, 5)
        timer.tick(100)
        pygame.display.update()
        pygame.guit()
