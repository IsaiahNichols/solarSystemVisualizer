#Solar System Visualizer
import utils
import random
import math
import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

dimensions = (900, 900)
screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption("SOLAR SYSTEM")

# Player Position
user_pos = [-dimensions[0]/2, -dimensions[1]/2]
zoom = 1
ZOOM_SPEED = 0.025
USER_SPEED = 10

def update_user_pos():
    global zoom
    global ZOOM_SPEED
    global user_pos
    keys = pygame.key.get_pressed()
    dir = [0, 0]

    dir[0] = keys[pygame.K_d] - keys[pygame.K_a]
    dir[1] = keys[pygame.K_s] - keys[pygame.K_w]

    user_hypo = math.sqrt(pow(dir[0], 2) + pow(dir[1], 2))

    for i in range(2):
        if user_hypo: dir[i] /= user_hypo

    user_pos[0] += dir[0] * USER_SPEED
    user_pos[1] += dir[1] * USER_SPEED

    mouse = pygame.mouse.get_pressed()
    
    if mouse[0]:
        zoom += ZOOM_SPEED
    if mouse[2]:
        zoom -= ZOOM_SPEED
    
    if keys[pygame.K_0]:
        user_pos = [-dimensions[0]/2, -dimensions[1]/2]

def user_main():
    update_user_pos()

# Game Objects
class Planet:
    def __init__(self, size: float, dist, speed, color: tuple) -> None:
        self.dist = dist
        self.pos = [0, 0]
        self.rel_pos = [0, 0]
        self.speed = speed
        self.size = size
        self.rel_size = size
        self.angle = math.radians(random.randint(0, 360))
        self.color = color
    
    def draw(self):
        pygame.draw.circle(screen, self.color, self.rel_pos, self.rel_size)

    def main(self):
        # Update Position
        global zoom

        self.pos[0] = math.cos(self.angle) * self.dist
        self.pos[1] = math.sin(self.angle) * self.dist

        self.angle += math.radians((2 * math.pi)/180) * self.speed

        for i in range(2):
            self.rel_pos[i] = (self.pos[i] - user_pos[i]) * zoom

        self.rel_size = self.size * zoom

        # Draw
        self.draw()


# --- Sun & Planets
sun = Planet(100, 0, 0, (255, 255, 0))
mercury = Planet(1.5, 200, 16, (155, 155, 155))
venus = Planet(4, 300, 14, (155, 155, 0))
earth = Planet(6, 400, 10, (0, 255, 0))
mars = Planet(3, 500, 8, (255, 0, 0))
jupiter = Planet(12, 600, 6, (255, 155, 155))
saturn = Planet(12, 700, 5, (100, 100, 20))
neptune = Planet(10, 800, 4, (0, 0, 255))
uranus = Planet(9, 900, 4, (0, 0, 100))
pluto = Planet(4, 1000, 1, (0, 0, 50))

planets = [sun, mercury, venus, earth, mars, jupiter, saturn, neptune, uranus, pluto]

# Game Loop
running = 1
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
    
    # Giving function to game objects
    for planet in planets:
        planet.main()
    
    user_main()

    clock.tick(FPS)
    pygame.display.flip()