#Solar System Visualizer
import pygame

pygame.init()

dimensions = (800, 800)
screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption("SOLAR SYSTEM")

# Game Objects
class Planet:
    def __init__(self, dist, size, speed) -> None:
        self.distance = dist
        self.size = size
        self.speed = speed
    
    def main(self):
        pass


# Game Loop
running = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0