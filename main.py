#Solar System Visualizer
import pygame

pygame.init()

dimensions = (800, 800)
screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption("SOLAR SYSTEM")

# Player Position
pos = [0, 0]
zoom = 1

# Game Objects
class Planet:
    def __init__(self, dist, size, speed) -> None:
        self.distance = dist
        self.size = size
        self.speed = speed
    
    def main(self):
        pass


# --- Planets
mercury = Planet()
venus = Planet()
earth = Planet()
mars = Planet()
jupiter = Planet()
saturn = Planet()
uranus = Planet()
neptune = Planet()

planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

# Game Loop
running = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
    
    for planet in planets:
        planet.main()