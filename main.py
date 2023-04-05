#Solar System Visualizer
import utils
import math
import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

dimensions = (800, 800)
screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption("SOLAR SYSTEM")

# Player Position
user_pos = [-dimensions[0]/2, -dimensions[1]/2]
zoom = 1
ZOOM_SPEED = 0.1
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
    def __init__(self, pos: list, size: int) -> None:
        self.pos = pos
        self.rel_pos = [0, 0]
        self.size = size
        self.rel_size = size
    
    def draw(self):
        pygame.draw.circle(screen, utils.WHITE, self.rel_pos, self.rel_size)

    def main(self):
        global zoom
        for i in range(2):
            self.rel_pos[i] = (self.pos[i] - user_pos[i]) * zoom

        self.rel_size = self.size * zoom

        self.draw()


# --- Planets
mercury = Planet([0, 0], 32)

planets = [mercury]

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