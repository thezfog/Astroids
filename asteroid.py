from constants import *
from circleshape import *
import random
import math
from constants import MIN_SPEED, MAX_SPEED

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        # Randomized velocity logic is embedded here
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.velocity = pygame.Vector2(
            speed * math.cos(angle),
            speed * math.sin(angle)
        )

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split():
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        
    